# ai-incident-lab

Languages: English | [中文](./README.zh-CN.md)

Runnable incident simulations for AI agents, MCP tools, and agent-generated code.

## Status

`P2` - reserved content and simulation foundation.

## Purpose

Create demos, workshops, and regression scenarios that make Safe Agent Operations concrete.

## First Production Surface

Local-only incident scenarios mapped to mcp-audit rules and reviewer lessons.

## Required Evidence

- scenario README
- safe reproduction steps
- expected finding mapping
- cleanup instructions
- teaching notes

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
- [OPT Overlay](./ops/opt-overlay.md)
- [Production Constraints](./ops/constraints/production.md)
- [Main Entry Constraints](./ops/constraints/main-entry.md)
- [Skill Evolution](./ops/skills/evolution.md)
