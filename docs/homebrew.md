# Homebrew Packaging

`ai-incident-lab` is distributed through the X-One tap.

## User Install

```bash
brew tap x-one-ai/tap
brew trust --formula x-one-ai/tap/ai-incident-lab
brew install x-one-ai/tap/ai-incident-lab
ai-incident-lab --version
```

## Tap Repository

```text
X-One-AI/homebrew-tap
```

Formula path:

```text
Formula/ai-incident-lab.rb
```

## Formula Requirements

- Install the Python CLI as `ai-incident-lab`.
- Use the released `xone-ai-incident-lab` source distribution.
- Vendor Python dependencies as Homebrew resources.
- Run `ai-incident-lab --version`, `init`, and `validate` in the formula test.

## Current Target

```text
xone-ai-incident-lab==0.2.0
```
