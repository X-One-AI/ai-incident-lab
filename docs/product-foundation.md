# ai-incident-lab Product Foundation

## Intake

- Priority: P2
- Status: v0.2.1 safe-local scenario CLI with bundled init flow
- Positioning: Runnable incident simulations for AI agents, MCP tools, and agent-generated code.
- Primary route: Product -> Architecture -> Expert/Security -> QA -> Implementation -> Completion readiness

## PRD

### Problem

Create safe local workshops and regression scenarios that make Safe Agent Operations concrete.

### Users

- Developers adopting AI agents or MCP tools
- Platform, DevTools, Security, and AI infrastructure teams
- Maintainers who need reviewable evidence rather than vague AI automation claims

### Goals

- scenario README
- safe reproduction steps
- expected finding mapping
- cleanup instructions
- teaching notes

### Non-Goals

- no real exploit kit
- no hosted sandbox first
- no unsafe secret-bearing fixtures

### Acceptance Criteria

- The project can explain its place in Safe Agent Operations in one sentence.
- The first production surface is local-first or review-first, not a hosted dashboard by default.
- Reports, packets, indexes, or labs must be redaction-safe by design.
- Every risky claim links to evidence, rule logic, or an explicit limitation.
- Scenarios use `ai-incident-lab.scenario.v1`.
- `ai-incident-lab validate --scenarios scenarios` validates the bundled scenario pack.
- `ai-incident-lab init --output ai-incident-scenarios` writes a bundled scenario pack for installed users.
- `ai-incident-lab render` produces Markdown and JSON runbooks.
- Scenario validation rejects secret-shaped placeholders, dangerous operations, and missing cleanup instructions.

## Architecture Brief

### Boundaries

- Keep shared workflow knowledge in OPT; keep project-specific decisions in this repository.
- Keep the main entrypoint small and explicit.
- Prefer file-based artifacts over hidden services for the first production surface.

### Data Flow

```text
scenario YAML + fixture files -> safe-local validation -> Markdown/JSON runbook
```

### Risks

- Overclaiming safety guarantees.
- Creating generic tooling that weakens the Agentic DevSecOps signal.
- Accepting real secrets or private user data into fixtures.

## QA Plan

- Unit-test redaction and dangerous-operation boundaries before scenario expansion.
- Add positive and negative fixtures for every behavior boundary.
- Verify generated artifacts do not include raw secrets.
- Keep bilingual README guidance aligned.

## Implementation Plan

1. Keep the first executable surface local and deterministic.
2. Use versioned `ai-incident-lab.scenario.v1` scenario YAML.
3. Require safe reproduction steps, expected findings, cleanup, teaching notes, and limitations.
4. Reject secret-shaped placeholders and dangerous operations.
5. Use feature branches named `feat/<scope>` or `docs/<scope>`.
6. Use Conventional/Angular commits such as `feat: add scenario pack` or `docs: clarify deferred scope`.
7. Never push directly to `main`; open a pull request from the feature branch.

## Skipped Inputs

- target audience
- sandbox policy
- first scenario requests
