from __future__ import annotations

import json
from typing import Any

from .schema import PACK_SCHEMA_VERSION


def render_json(scenarios: list[dict[str, Any]]) -> str:
    return json.dumps({"schema_version": PACK_SCHEMA_VERSION, "scenarios": scenarios}, ensure_ascii=False, indent=2) + "\n"


def render_markdown(scenarios: list[dict[str, Any]]) -> str:
    lines = [
        "# AI Incident Lab Runbook",
        "",
        f"Schema: `{PACK_SCHEMA_VERSION}`",
        "",
    ]
    for scenario in scenarios:
        lines.extend(_render_scenario(scenario))
    lines.extend(
        [
            "## Lab Limitations",
            "",
            "- Scenarios are safe local review exercises, not exploit kits.",
            "- Labs teach review behavior and expected evidence, not runtime protection.",
            "- Fixture data must remain synthetic and redaction-safe.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_scenario(scenario: dict[str, Any]) -> list[str]:
    lines = [
        f"## {scenario['title']}",
        "",
        f"- ID: `{scenario['id']}`",
        f"- Safety level: `{scenario['safety_level']}`",
        f"- Incident type: `{scenario['incident_type']}`",
        f"- Objective: {scenario['objective']}",
        "",
        "### Steps",
        "",
    ]
    for index, step in enumerate(scenario["steps"], start=1):
        lines.append(f"{index}. {step}")

    lines.extend(["", "### Expected Findings", ""])
    for finding in scenario["expected_findings"]:
        lines.append(f"- `{finding['id']}`: {finding['description']}")

    if scenario.get("remediation_steps"):
        lines.extend(["", "### Remediation Steps", ""])
        for item in scenario["remediation_steps"]:
            lines.append(f"- {item}")

    lines.extend(["", "### Cleanup", ""])
    for item in scenario["cleanup"]:
        lines.append(f"- {item}")

    lines.extend(["", "### Teaching Notes", ""])
    for item in scenario["teaching_notes"]:
        lines.append(f"- {item}")

    lines.extend(["", "### Limitations", ""])
    for item in scenario["limitations"]:
        lines.append(f"- {item}")
    lines.append("")
    return lines
