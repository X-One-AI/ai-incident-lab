# Core Tool Training Workflow

`ai-incident-lab` supports X-One by turning the core tools into safe-local workshop, demo, and regression exercises. It is a support asset, not the primary product users adopt every day.

## core tool training path

1. Pick one core tool goal:
   - `mcp-audit`: review MCP config scope and policy decisions.
   - `agent-pr-evidence`: review AI-agent PR evidence before merge.
   - `agent-failure-packet`: produce a redacted failure packet for issue handoff.
2. Initialize a local scenario pack:

   ```bash
   ai-incident-lab init --output ai-incident-scenarios
   ```

3. Validate scenarios before the workshop:

   ```bash
   ai-incident-lab validate --scenarios ai-incident-scenarios
   ```

4. Render a runbook and map each expected finding back to the relevant core tool:

   ```bash
   ai-incident-lab render --scenarios ai-incident-scenarios --format markdown --output ai-incident-runbook.md
   ```

5. End the session with one concrete adoption action: a policy check, reviewer evidence gate, or redacted issue packet.

## Support asset, not a primary product

The lab must remain:

- safe-local;
- scenario-based;
- mapped to core tool behavior;
- free of exploit-kit, hosted sandbox, or runtime protection claims.

## Product gate

This support asset is production-ready only when:

- every scenario maps to `mcp-audit`, `agent-pr-evidence`, or `agent-failure-packet`;
- workshop users can complete setup and render a runbook in 10 minutes;
- unsafe commands, real secrets, and destructive cleanup are blocked by validation;
- scenario feedback feeds back into core tool docs, fixtures, or tests.
