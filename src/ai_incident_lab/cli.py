from __future__ import annotations

import argparse
import sys
from importlib import resources
from pathlib import Path
from shutil import copytree
from typing import Sequence

from . import __version__
from .renderers import render_json, render_markdown
from .scenarios import ScenarioValidationError, load_scenarios


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            source = resources.files("ai_incident_lab").joinpath("scenario_pack")
            copytree(source, args.output, dirs_exist_ok=args.force)
            print(f"wrote {args.output}")
            return 0

        if args.command == "list":
            for scenario in load_scenarios(args.scenarios):
                print(f"{scenario['id']}\t{scenario['title']}\t{scenario['safety_level']}")
            return 0

        if args.command == "validate":
            scenarios = load_scenarios(args.scenarios)
            print(f"schema_version=ai-incident-lab.scenario.v1 scenarios={len(scenarios)}")
            return 0

        if args.command == "render":
            scenarios = load_scenarios(args.scenarios)
            output = render_markdown(scenarios) if args.format == "markdown" else render_json(scenarios)
            if args.output:
                args.output.write_text(output, encoding="utf-8")
            else:
                print(output, end="")
            return 0

        parser.print_help()
        return 2
    except ScenarioValidationError as exc:
        print(f"ai-incident-lab: {exc}", file=sys.stderr)
        return 1


def entrypoint() -> None:
    raise SystemExit(main())


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-incident-lab",
        description="Validate and render safe local incident scenarios for AI agent workflows.",
    )
    parser.add_argument("--version", action="version", version=f"ai-incident-lab {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    init = subparsers.add_parser("init", help="Write the bundled safe-local scenario pack.")
    init.add_argument("--output", required=True, type=Path, help="Target scenario directory.")
    init.add_argument("--force", action="store_true", help="Overwrite files in an existing directory.")

    list_cmd = subparsers.add_parser("list", help="List scenario ids and titles.")
    list_cmd.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")

    validate = subparsers.add_parser("validate", help="Validate safe-local scenario files.")
    validate.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")

    render = subparsers.add_parser("render", help="Render scenarios as a runbook.")
    render.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")
    render.add_argument("--format", required=True, choices=("markdown", "json"), help="Output format.")
    render.add_argument("--output", type=Path, help="Output file. Writes to stdout when omitted.")

    return parser
