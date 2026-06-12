# AI Incident Lab Runbook

Schema: `ai-incident-lab.pack.v1`

## MCP Wide Filesystem Scope

- ID: `mcp-wide-filesystem-scope`
- Safety level: `safe-local`
- Incident type: `mcp-config-risk`
- Objective: Teach reviewers to identify over-broad filesystem MCP access without touching real user files.

### Steps

1. Inspect the fixture config in `fixtures/mcp-wide-filesystem-scope/mcp.json`.
2. Confirm the filesystem server is pointed at `/tmp/ai-incident-lab-wide-scope`.
3. Compare that scope with the narrower expected project path in the teaching notes.

### Expected Findings

- `wide-filesystem-scope`: Filesystem MCP access is broader than the intended project-only review surface.

### Cleanup

- Delete `/tmp/ai-incident-lab-wide-scope` if you created it during a workshop.

### Teaching Notes

- The scenario uses `/tmp`, not a real home directory or workspace root.
- The lesson maps to MCP configuration review, not runtime sandbox enforcement.

### Limitations

- This lab does not execute the MCP server.
- It demonstrates review reasoning, not exploitability.

## Agent PR Missing Verification

- ID: `agent-pr-missing-verification`
- Safety level: `safe-local`
- Incident type: `agent-pr-review`
- Objective: Teach reviewers to reject agent-generated PRs that lack test evidence and risk notes.

### Steps

1. Open `fixtures/agent-pr-missing-verification/pr-summary.md`.
2. Identify missing test evidence, missing rollback notes, and vague scope language.
3. Draft the minimum reviewer follow-up required before merge.

### Expected Findings

- `missing-test-evidence`: PR summary claims completion without showing a verification command or result.
- `missing-risk-summary`: PR summary does not mention config, dependency, auth, or CI risk.

### Cleanup

- No generated files. Close the fixture after review.

### Teaching Notes

- The scenario reinforces evidence-before-merge rather than agent distrust.
- Reviewers should ask for concrete command output, not broad reassurance.

### Limitations

- This lab uses a static PR summary fixture.
- It does not call the GitHub API.

## Agent Log Secret Exposure

- ID: `agent-log-secret-exposure`
- Safety level: `safe-local`
- Incident type: `redaction-failure`
- Objective: Teach maintainers to recognize secret-shaped log exposure without storing a real secret.

### Steps

1. Open `fixtures/agent-log-secret-exposure/agent-log.txt`.
2. Find the redacted token placeholder and confirm it is not a real credential.
3. Explain which log fields should be removed before sharing a failure packet.

### Expected Findings

- `secret-shaped-log-output`: Agent logs can expose credential-shaped values and must be redacted before sharing.

### Cleanup

- No generated files. Close the fixture after review.

### Teaching Notes

- The fixture uses `TOKEN_REDACTED_EXAMPLE`, not a real token.
- The lesson maps to redaction and failure packet sharing.

### Limitations

- This lab does not test a live secret scanner.
- It is a human review scenario.

## Lab Limitations

- Scenarios are safe local review exercises, not exploit kits.
- Labs teach review behavior and expected evidence, not runtime protection.
- Fixture data must remain synthetic and redaction-safe.
