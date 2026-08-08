# Security and secrets boundary

**RM-CONFIG-SECURITY-0001:** Configuration carries policy inputs; it does not grant authority. A configured path, endpoint, account name, or feature flag cannot substitute for an authorized capability.

**RM-CONFIG-SECURITY-0002:** Secret material is prohibited in ordinary snapshots, provenance, diagnostics, change events, logs, crash reports, and benchmark fixtures. Configuration may carry a typed reference resolved through the secret-store capability under separate authority.

**RM-CONFIG-SECURITY-0003:** Source authority is least privilege and separates read, observe, and write. Observing a source does not imply permission to modify it.

**RM-CONFIG-SECURITY-0004:** Untrusted configuration is size/depth bounded, schema validated, and safe for diagnostic rendering. Native parse errors and source locations are sanitized before crossing trust boundaries.

**RM-CONFIG-SECURITY-0005:** Administrator-enforced values and user values remain distinguishable. A locked value cannot be overridden through a lower-trust source, session input, or migration.

**RM-CONFIG-SECURITY-0006:** Writes, when separately selected, use compare/revision preconditions where available and never promise cross-source atomic transactions. Durable publication claims depend on filesystem or native-store evidence.

Threats include configuration injection, symlink/reparse redirection, parser resource exhaustion, downgrade through stale sources, malicious hot reload, diagnostic leakage, and authority laundering through path-like values.

