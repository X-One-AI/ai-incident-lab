SCENARIO_SCHEMA_VERSION = "ai-incident-lab.scenario.v1"
PACK_SCHEMA_VERSION = "ai-incident-lab.pack.v1"

REQUIRED_FIELDS = {
    "schema_version",
    "id",
    "order",
    "title",
    "safety_level",
    "summary",
    "incident_type",
    "objective",
    "setup",
    "steps",
    "expected_findings",
    "rule_mappings",
    "cleanup",
    "teaching_notes",
    "limitations",
    "redaction_notes",
}

DANGEROUS_PATTERNS = (
    "rm -rf /",
    "mkfs",
    "dd if=",
    ":(){",
    "shutdown",
    "reboot",
    "curl | sh",
    "wget | sh",
)

SECRET_PATTERNS = (
    "sk-live-",
    "ghp_",
    "github_pat_",
    "AKIA",
    "BEGIN PRIVATE KEY",
)


class ScenarioValidationError(ValueError):
    """Raised when a scenario violates the safe-local lab contract."""
