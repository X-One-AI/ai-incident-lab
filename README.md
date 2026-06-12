# ai-incident-lab

Languages: English | [中文](./README.zh-CN.md)

Runnable incident simulations for AI agents, MCP tools, and agent-generated code.

## Status

`v0.1.0` - safe-local scenario CLI and first incident pack.

## Purpose

Create safe local workshops and regression scenarios that make Safe Agent Operations concrete.

## First Production Surface

Local-only incident scenarios mapped to X-One tools, expected findings, cleanup steps, and reviewer lessons.

```bash
python3 -m pip install xone-ai-incident-lab
ai-incident-lab list --scenarios scenarios
ai-incident-lab validate --scenarios scenarios
ai-incident-lab render --scenarios scenarios --format markdown --output ai-incident-runbook.md
ai-incident-lab render --scenarios scenarios --format json --output ai-incident-runbook.json
```

For local development:

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
```

## Required Evidence

- scenario README
- safe reproduction steps
- expected finding mapping
- cleanup instructions
- teaching notes

## Scenario Contract

Scenarios use `ai-incident-lab.scenario.v1` and must remain `safe-local`. They are review exercises, not exploit kits or runtime protection.

## Non-Goals

- no real exploit kit
- no hosted sandbox first
- no unsafe secret-bearing fixtures

## OPT Operating Model

This project references the shared One Person Team workflow through [ops/opt-overlay.md](./ops/opt-overlay.md). Project-specific constraints live under [ops/constraints](./ops/constraints), and evolvable local skills live under [ops/skills](./ops/skills).

## Blocked Inputs

Inputs that require user or real-world data are recorded in `../x-one-skipped-inputs.md` and should not block foundation work.

## Docs

- [Product Foundation](./docs/product-foundation.md)
- [Scenario Lab Design](./docs/scenario-lab-design.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [Production Constraints](./ops/constraints/production.md)
- [Main Entry Constraints](./ops/constraints/main-entry.md)
- [Skill Evolution](./ops/skills/evolution.md)
