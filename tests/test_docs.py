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
    assert "ai-incident-lab render" in english
    assert "v0.1.0" in english
    assert "README.zh-CN.md" in english
    assert "ai-incident-lab validate" in chinese
    assert "ai-incident-lab render" in chinese
    assert "v0.1.0" in chinese
    assert "README.md" in chinese
    assert "ai-incident-lab.scenario.v1" in foundation
    assert "safe-local" in spec
    assert "python3 -m pytest tests -q" in ci
    assert 'version = "0.1.0"' in pyproject
    assert "## 0.1.0" in changelog
