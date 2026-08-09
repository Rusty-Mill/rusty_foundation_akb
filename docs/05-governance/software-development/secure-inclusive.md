# Security, privacy, accessibility, i18n, and observability

**RM-DEV-QUAL-0001:** Every change identifies affected authority, trust, sensitive data, tenant/user boundaries, native resources, external inputs, effects, and failure modes. Unaffected claims require reviewable rationale for material changes.

**RM-DEV-QUAL-0002:** Validate external input at the boundary; use deny-by-default authority, least privilege, explicit inheritance/delegation, secure defaults, bounded resources, and authenticated provenance. Secrets never enter source, logs, panic text, snapshots, fixtures, or build artifacts.

**RM-DEV-QUAL-0003:** Threat/privacy review addresses misuse, confused deputy, injection, memory/resource exhaustion, races, downgrade/fallback, disclosure/linkability, retention, rights/erasure, incident evidence, and provider/supply-chain compromise as applicable.

**RM-DEV-QUAL-0004:** User-facing functionality includes keyboard/non-pointer paths, semantic accessibility, focus/order/status/error behavior, assistive-technology/native adapter evidence, preferences, reduced motion/contrast, and nonvisual operation where applicable.

**RM-DEV-QUAL-0005:** User-facing text is externalized, typed, localizable, and accessible. Logic does not parse localized presentation. Locale, time zone, calendar, collation, numbering, directionality, encoding, Unicode data/version, and live-change policy are explicit.

**RM-DEV-QUAL-0006:** Structured telemetry uses stable event/field identities, causal context, privacy classification, bounded cardinality/volume, backpressure/drop policy, configurable export, and measurable overhead. Diagnostics are not domain truth or authority.

**RM-DEV-QUAL-0007:** Logs and errors contain actionable boundary/operation/outcome context without credentials, secret values, unnecessary personal data, or unbounded attacker-controlled content.

**RM-DEV-QUAL-0008:** Security, privacy, accessibility, i18n, observability, and operational reviewers can block a change within their authority; waivers follow the common exception process and cannot waive undeclared safety invariants.
