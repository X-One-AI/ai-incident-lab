# ai-incident-lab

Languages: English | [中文](./README.zh-CN.md)

Runnable incident simulations for AI agents, MCP tools, and agent-generated code.

## Status

`v0.2.2` - safe-local scenario CLI, bundled scenario pack, remediation steps, and first-run init flow.

## Purpose

Create safe local workshops and regression scenarios that make Safe Agent Operations concrete.

## First Production Surface

Local-only incident scenarios mapped to X-One tools, expected findings, remediation steps, cleanup steps, and reviewer lessons.

From PyPI:

```bash
python3 -m pip install xone-ai-incident-lab
ai-incident-lab init --output ai-incident-scenarios
ai-incident-lab list --scenarios ai-incident-scenarios
ai-incident-lab validate --scenarios ai-incident-scenarios
ai-incident-lab render --scenarios ai-incident-scenarios --format markdown --output ai-incident-runbook.md
ai-incident-lab render --scenarios ai-incident-scenarios --format json --output ai-incident-runbook.json
```

From Homebrew:

```bash
brew install x-one-ai/tap/ai-incident-lab
ai-incident-lab --version
```

For local development:

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
ai-incident-lab validate --scenarios scenarios
```

## Required Evidence

- scenario README
- safe reproduction steps
- expected finding mapping
- remediation steps
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

Real-user feedback should be classified as false-positive, false-negative, adapter-request, scenario-request, or catalog-update when it applies; portfolio-level handling is tracked in X-One portfolio health docs.

## Docs

- [Product Foundation](./docs/product-foundation.md)
- [Scenario Lab Design](./docs/scenario-lab-design.md)
- [Core Tool Training Workflow](./docs/core-tool-training-workflow.md)
- [Publishing](./docs/publishing.md)
- [Homebrew Packaging](./docs/homebrew.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [Production Constraints](./ops/constraints/production.md)
- [Main Entry Constraints](./ops/constraints/main-entry.md)
- [Skill Evolution](./ops/skills/evolution.md)
