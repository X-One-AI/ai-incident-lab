# ai-incident-lab

语言： [English](./README.md) | 中文

面向 AI agents、MCP tools 和 agent-generated code 的可运行事故模拟。

## 状态

`v0.2.1` - safe-local 场景 CLI、内置场景包和首次使用 init 流程。

## 目的

创建安全的本地 workshop 和回归场景，让 Safe Agent Operations 变得具体可练习。

## 第一生产化表面

本地 incident scenarios：映射到 X-One 工具、预期发现、清理步骤和 reviewer lessons。

从 PyPI 安装：

```bash
python3 -m pip install xone-ai-incident-lab
ai-incident-lab init --output ai-incident-scenarios
ai-incident-lab list --scenarios ai-incident-scenarios
ai-incident-lab validate --scenarios ai-incident-scenarios
ai-incident-lab render --scenarios ai-incident-scenarios --format markdown --output ai-incident-runbook.md
ai-incident-lab render --scenarios ai-incident-scenarios --format json --output ai-incident-runbook.json
```

从 Homebrew 安装：

```bash
brew install x-one-ai/tap/ai-incident-lab
ai-incident-lab --version
```

本地开发：

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
ai-incident-lab validate --scenarios scenarios
```

## 必要证据

- scenario README
- safe reproduction steps
- expected finding mapping
- cleanup instructions
- teaching notes

## Scenario 契约

场景使用 `ai-incident-lab.scenario.v1`，并且必须保持 `safe-local`。它们是 review 练习，不是 exploit kit，也不提供 runtime protection。

## 非目标

- no real exploit kit
- no hosted sandbox first
- no unsafe secret-bearing fixtures

## OPT 运行模型

本项目通过 [ops/opt-overlay.md](./ops/opt-overlay.md) 引用共享 One Person Team 工作流。项目自己的约束放在 [ops/constraints](./ops/constraints)，可演进 skill 放在 [ops/skills](./ops/skills)。

## 暂缺输入

需要用户或真实世界数据补充的内容记录在 `../x-one-skipped-inputs.md`，不阻塞基础建设。

真实用户反馈在适用时应分类为 false-positive、false-negative、adapter-request、scenario-request 或 catalog-update；组合层面的处理由 X-One portfolio health docs 跟踪。

## 文档

- [产品基础](./docs/product-foundation.md)
- [Scenario Lab Design](./docs/scenario-lab-design.md)
- [Core Tool Training Workflow](./docs/core-tool-training-workflow.md)
- [Publishing](./docs/publishing.md)
- [Homebrew Packaging](./docs/homebrew.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [生产约束](./ops/constraints/production.md)
- [主入口约束](./ops/constraints/main-entry.md)
- [Skill 演进](./ops/skills/evolution.md)
