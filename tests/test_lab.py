import json
import subprocess
import sys
from pathlib import Path

import pytest

from ai_incident_lab.cli import main
from ai_incident_lab.scenarios import ScenarioValidationError, load_scenarios
from ai_incident_lab.renderers import render_json, render_markdown


SCENARIOS = Path("scenarios")


def test_load_scenarios_validates_bundled_pack():
    scenarios = load_scenarios(SCENARIOS)

    assert [scenario["id"] for scenario in scenarios] == [
        "mcp-wide-filesystem-scope",
        "agent-pr-missing-verification",
        "agent-log-secret-exposure",
        "agent-evidence-loop",
    ]
    assert all(scenario["safety_level"] == "safe-local" for scenario in scenarios)
    assert all(scenario["remediation_steps"] for scenario in scenarios)


@pytest.mark.parametrize(
    "fixture, message",
    [
        ("tests/fixtures/invalid-secret.yml", "placeholder secret"),
        ("tests/fixtures/invalid-dangerous-step.yml", "dangerous operation"),
        ("tests/fixtures/invalid-missing-cleanup.yml", "cleanup"),
    ],
)
def test_invalid_scenarios_fail_with_clear_errors(fixture, message):
    with pytest.raises(ScenarioValidationError, match=message):
        load_scenarios(Path(fixture))


def test_render_markdown_snapshot_stays_stable():
    expected = Path("tests/fixtures/snapshots/scenarios.md").read_text(encoding="utf-8")

    assert render_markdown(load_scenarios(SCENARIOS)) == expected


def test_render_json_is_machine_readable():
    data = json.loads(render_json(load_scenarios(SCENARIOS)))

    assert data["schema_version"] == "ai-incident-lab.pack.v1"
    assert data["scenarios"][0]["id"] == "mcp-wide-filesystem-scope"
    assert data["scenarios"][0]["remediation_steps"]


def test_render_markdown_outputs_remediation_steps():
    markdown = render_markdown(load_scenarios(SCENARIOS))

    assert "### Remediation Steps" in markdown
    assert "Narrow the filesystem scope" in markdown


def test_cli_list_validate_and_render(tmp_path, capsys):
    initialized = tmp_path / "scenarios"
    markdown = tmp_path / "runbook.md"
    json_output = tmp_path / "runbook.json"

    init_exit = main(["init", "--output", str(initialized)])
    list_exit = main(["list", "--scenarios", str(SCENARIOS)])
    validate_exit = main(["validate", "--scenarios", str(SCENARIOS)])
    markdown_exit = main(["render", "--scenarios", str(SCENARIOS), "--format", "markdown", "--output", str(markdown)])
    json_exit = main(["render", "--scenarios", str(SCENARIOS), "--format", "json", "--output", str(json_output)])

    captured = capsys.readouterr()
    assert init_exit == 0
    assert load_scenarios(initialized)
    assert list_exit == 0
    assert "mcp-wide-filesystem-scope" in captured.out
    assert validate_exit == 0
    assert "scenarios=4" in captured.out
    assert markdown_exit == 0
    assert json_exit == 0
    assert "# AI Incident Lab Runbook" in markdown.read_text(encoding="utf-8")
    assert json.loads(json_output.read_text(encoding="utf-8"))["scenarios"]


def test_package_module_entrypoint_outputs_version():
    result = subprocess.run(
        [sys.executable, "-m", "ai_incident_lab", "--version"],
        check=True,
        env={"PYTHONPATH": "src"},
        text=True,
        stdout=subprocess.PIPE,
    )

    assert result.stdout.strip() == "ai-incident-lab 0.2.2"


def test_agent_evidence_loop_scenario_maps_x_one_tools():
    scenarios = load_scenarios(Path("scenarios"))
    scenario = next(item for item in scenarios if item["id"] == "agent-evidence-loop")
    rendered = render_markdown([scenario])

    assert "agent-pr-evidence" in rendered
    assert "agent-failure-packet" in rendered
    assert "mcp-risk-index" in rendered
    assert "This scenario teaches the evidence loop. It does not execute the other X-One tools." in rendered
