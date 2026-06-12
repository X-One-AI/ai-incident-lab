# Scenario Lab Design

## Status

Implemented for v0.1.0.

## Product Decision

`ai-incident-lab` is a safe-local scenario pack for teaching and regression review. It is not an exploit kit, live sandbox, or runtime protection product.

## First Production Surface

Local CLI:

```bash
ai-incident-lab list --scenarios scenarios
ai-incident-lab validate --scenarios scenarios
ai-incident-lab render --scenarios scenarios --format markdown --output ai-incident-runbook.md
```

## Scenario Contract

Each scenario uses `ai-incident-lab.scenario.v1` and must include:

- `safety_level: safe-local`
- setup and review steps
- stable `order` for runbook sequencing
- expected findings
- mapping to an X-One tool or rule family
- cleanup instructions
- teaching notes
- limitations
- redaction notes

## Safety Gate

- No real secrets or secret-shaped placeholders.
- No destructive shell operations.
- No exploit instructions.
- No hosted sandbox in v0.1.0.
- No claim of runtime protection.

## OPT Link

This repo references shared OPT through `ops/opt-overlay.md`. Scenario design rules and local safety constraints live in this repository because they are product-specific.
