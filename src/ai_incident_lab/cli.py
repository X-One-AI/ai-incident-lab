from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from . import __version__
from .renderers import render_json, render_markdown
from .scenarios import ScenarioValidationError, load_scenarios


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
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

    list_cmd = subparsers.add_parser("list", help="List scenario ids and titles.")
    list_cmd.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")

    validate = subparsers.add_parser("validate", help="Validate safe-local scenario files.")
    validate.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")

    render = subparsers.add_parser("render", help="Render scenarios as a runbook.")
    render.add_argument("--scenarios", required=True, type=Path, help="Scenario directory or YAML file.")
    render.add_argument("--format", required=True, choices=("markdown", "json"), help="Output format.")
    render.add_argument("--output", type=Path, help="Output file. Writes to stdout when omitted.")

    return parser
