# Definitions, registration, and enablement

A `BackgroundDefinition` is immutable and versioned. It names workload kind, stable product-owned identity, package/executable generation, arguments and environment schema, scope, principal policy, triggers, restart/retry policy, budgets, dependency endpoints, update/removal behavior, observability/privacy policy, and compatibility range.

**RM-BACKGROUND-DEFINITION-0001:** Demand service, persistent service, session agent, login item, finite task, maintenance job, and durable schedule MUST remain distinct workload kinds with separately negotiated platform mappings.

**RM-BACKGROUND-DEFINITION-0002:** Definitions MUST bind a verified immutable package/executable generation and structured launch configuration. Ambient executable search, shell parsing, mutable working-directory lookup, and inherited caller environment are forbidden.

**RM-BACKGROUND-DEFINITION-0003:** Registration is a privileged transactional operation with exact target scope, expected prior generation, installer identity, authority, validation report, commit point, rollback plan, and resulting native registration evidence.

**RM-BACKGROUND-DEFINITION-0004:** `installed`, `registered`, `enabled`, `trigger_armed`, `start_requested`, `running`, `ready`, `stopping`, and `removed` MUST be independent states; one MUST NOT imply another.

**RM-BACKGROUND-DEFINITION-0005:** User, administrator, enterprise, and operating-system policy may disable, alter, defer, quarantine, or remove a registration. Observation reports provenance and current effective state without silently repairing it.

**RM-BACKGROUND-DEFINITION-0006:** Native identifiers and labels MUST be namespaced, collision-checked, length/grammar validated, and bound to product/package identity; registration cannot overwrite an unrelated owner.

**RM-BACKGROUND-DEFINITION-0007:** Registration, enablement, reconfiguration, and removal MUST be idempotent against an expected generation and MUST expose partial or ambiguous commit rather than assuming success.
