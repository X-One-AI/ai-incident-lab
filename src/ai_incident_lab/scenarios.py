from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .schema import (
    DANGEROUS_PATTERNS,
    REQUIRED_FIELDS,
    SCENARIO_SCHEMA_VERSION,
    SECRET_PATTERNS,
    ScenarioValidationError,
)


def load_scenarios(path: Path | str) -> list[dict[str, Any]]:
    scenario_path = Path(path)
    if scenario_path.is_dir():
        scenarios = [_load_one(file_path) for file_path in sorted(scenario_path.glob("*.yml"))]
    else:
        scenarios = [_load_one(scenario_path)]
    if not scenarios:
        raise ScenarioValidationError(f"No scenario YAML files found: {scenario_path}")
    seen_ids: set[str] = set()
    for scenario in scenarios:
        _validate_scenario(scenario, seen_ids=seen_ids)
    return sorted(scenarios, key=lambda item: item["order"])


def _load_one(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ScenarioValidationError(f"Scenario not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise ScenarioValidationError(f"Scenario is not valid YAML: {path}") from exc
    if not isinstance(data, dict):
        raise ScenarioValidationError(f"Scenario root must be a mapping: {path}")
    return data


def _validate_scenario(scenario: dict[str, Any], *, seen_ids: set[str]) -> None:
    missing = sorted(REQUIRED_FIELDS.difference(scenario))
    if missing:
        raise ScenarioValidationError(f"Scenario is missing required field: {missing[0]}")

    if scenario["schema_version"] != SCENARIO_SCHEMA_VERSION:
        raise ScenarioValidationError(f"Unsupported scenario schema_version: {scenario['schema_version']!r}")
    scenario_id = scenario["id"]
    if not isinstance(scenario_id, str) or not scenario_id:
        raise ScenarioValidationError("Scenario id must be a non-empty string")
    if scenario_id in seen_ids:
        raise ScenarioValidationError(f"Duplicate scenario id: {scenario_id}")
    seen_ids.add(scenario_id)

    if scenario["safety_level"] != "safe-local":
        raise ScenarioValidationError(f"Scenario {scenario_id} must use safety_level safe-local")
    if not isinstance(scenario["order"], int) or scenario["order"] <= 0:
        raise ScenarioValidationError(f"Scenario {scenario_id} order must be a positive integer")

    for field in ("setup", "steps", "cleanup", "teaching_notes", "limitations", "redaction_notes"):
        _require_string_list(scenario, field, scenario_id=scenario_id)

    if not scenario["cleanup"]:
        raise ScenarioValidationError(f"Scenario {scenario_id} must include cleanup instructions")

    findings = scenario["expected_findings"]
    if not isinstance(findings, list) or not findings:
        raise ScenarioValidationError(f"Scenario {scenario_id} must include expected findings")
    for finding in findings:
        if not isinstance(finding, dict) or not finding.get("id") or not finding.get("description"):
            raise ScenarioValidationError(f"Scenario {scenario_id} has an invalid expected finding")

    mappings = scenario["rule_mappings"]
    if not isinstance(mappings, list) or not mappings:
        raise ScenarioValidationError(f"Scenario {scenario_id} must include rule mappings")
    for mapping in mappings:
        if not isinstance(mapping, dict) or not mapping.get("tool") or not mapping.get("rule"):
            raise ScenarioValidationError(f"Scenario {scenario_id} has an invalid rule mapping")

    text = yaml.safe_dump(scenario, sort_keys=True)
    for pattern in SECRET_PATTERNS:
        if pattern in text:
            raise ScenarioValidationError(f"Scenario {scenario_id} contains a placeholder secret pattern: {pattern}")
    for pattern in DANGEROUS_PATTERNS:
        if pattern in text:
            raise ScenarioValidationError(f"Scenario {scenario_id} contains a dangerous operation: {pattern}")


def _require_string_list(scenario: dict[str, Any], field: str, *, scenario_id: str) -> None:
    value = scenario[field]
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ScenarioValidationError(f"Scenario {scenario_id} field {field} must be a list of strings")
