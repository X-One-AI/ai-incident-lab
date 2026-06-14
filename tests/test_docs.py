from pathlib import Path


def test_docs_package_and_ci_stay_aligned():
    english = Path("README.md").read_text(encoding="utf-8")
    chinese = Path("README.zh-CN.md").read_text(encoding="utf-8")
    foundation = Path("docs/product-foundation.md").read_text(encoding="utf-8")
    spec = Path("docs/scenario-lab-design.md").read_text(encoding="utf-8")
    ci = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    changelog = Path("CHANGELOG.md").read_text(encoding="utf-8")

    assert "ai-incident-lab validate" in english
    assert "ai-incident-lab init" in english
    assert "ai-incident-lab render" in english
    assert "v0.2.2" in english
    assert "README.zh-CN.md" in english
    assert "ai-incident-lab validate" in chinese
    assert "ai-incident-lab init" in chinese
    assert "ai-incident-lab render" in chinese
    assert "v0.2.2" in chinese
    assert "README.md" in chinese
    assert "ai-incident-lab.scenario.v1" in foundation
    assert "safe-local" in spec
    assert "python3 -m pytest tests -q" in ci
    assert 'version = "0.2.2"' in pyproject
    assert "__version__ = \"0.2.2\"" in Path("src/ai_incident_lab/__init__.py").read_text(encoding="utf-8")
    assert "## 0.2.2" in changelog
    assert "## 0.1.0" in changelog


def test_core_tool_training_workflow_is_actionable():
    workflow = Path("docs/core-tool-training-workflow.md").read_text(encoding="utf-8")

    assert "core tool training path" in workflow
    assert "mcp-audit" in workflow
    assert "agent-pr-evidence" in workflow
    assert "agent-failure-packet" in workflow
    assert "Support asset, not a primary product" in workflow
    assert "Product gate" in workflow
