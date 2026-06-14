# Publishing

`ai-incident-lab` uses GitHub Actions and PyPI Trusted Publishing.

Python distribution package:

```text
xone-ai-incident-lab
```

Installed CLI:

```text
ai-incident-lab
```

## Current Index Status

As of 2026-06-14, public API checks show:

- PyPI: `xone-ai-incident-lab 0.2.1` is published with 2 artifacts.
- TestPyPI: `xone-ai-incident-lab 0.2.1` is published with 2 artifacts.

## GitHub Environments

Create these GitHub environments:

- `testpypi`
- `pypi`

The `pypi` environment should require manual approval.

## Trusted Publisher Settings

```text
Project: xone-ai-incident-lab
Owner: X-One-AI
Repository: ai-incident-lab
Workflow: publish.yml
Environment: testpypi or pypi
```

## Publish Order

1. Merge and verify a green CI run on `main`.
2. Confirm the release tag exists, for example `v0.2.2`.
3. Run `Publish Python Package` with `repository = testpypi`.
4. Verify a clean TestPyPI install.
5. Run `Publish Python Package` with `repository = pypi` from a release tag after approval.
6. Verify a clean PyPI install.

## TestPyPI Install Check

```bash
python -m venv /tmp/ai-incident-lab-testpypi
/tmp/ai-incident-lab-testpypi/bin/python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  xone-ai-incident-lab
/tmp/ai-incident-lab-testpypi/bin/ai-incident-lab --version
```

## PyPI Install Check

```bash
python -m venv /tmp/ai-incident-lab-pypi
/tmp/ai-incident-lab-pypi/bin/python -m pip install xone-ai-incident-lab
/tmp/ai-incident-lab-pypi/bin/ai-incident-lab --version
```

## GitHub Release Install Path

```bash
python3 -m pip install https://github.com/X-One-AI/ai-incident-lab/releases/download/v0.2.2/xone_ai_incident_lab-0.2.2-py3-none-any.whl
ai-incident-lab --version
```
