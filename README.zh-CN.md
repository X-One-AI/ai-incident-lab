# ai-incident-lab

语言： [English](./README.md) | 中文

面向 AI agents、MCP tools 和 agent-generated code 的可运行事故模拟。

## 状态

`P2` - reserved content and simulation foundation。

## 目的

Create demos, workshops, and regression scenarios that make Safe Agent Operations concrete.

## 第一生产化表面

Local-only incident scenarios mapped to mcp-audit rules and reviewer lessons.

## 必要证据

- scenario README
- safe reproduction steps
- expected finding mapping
- cleanup instructions
- teaching notes

## 非目标

- no real exploit kit
- no hosted sandbox first
- no unsafe secret-bearing fixtures

## OPT 运行模型

本项目通过 [ops/opt-overlay.md](./ops/opt-overlay.md) 引用共享 One Person Team 工作流。项目自己的约束放在 [ops/constraints](./ops/constraints)，可演进 skill 放在 [ops/skills](./ops/skills)。

## 暂缺输入

需要用户或真实世界数据补充的内容记录在 `../x-one-skipped-inputs.md`，不阻塞基础建设。

## 文档

- [产品基础](./docs/product-foundation.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [生产约束](./ops/constraints/production.md)
- [主入口约束](./ops/constraints/main-entry.md)
- [Skill 演进](./ops/skills/evolution.md)
