# Audit event schema and semantics

**RM-AUDIT-EVENT-0001:** Event identity includes stable event ID, event type/schema/version, source system/component/instance generation, tenant/account, correlation/trace/workflow/case IDs, and duplicate lineage.

**RM-AUDIT-EVENT-0002:** Actor fields distinguish initiating subject, authenticated account/session, effective/delegated identity, workload/service, human operator, approver, authorizing policy/decision, and impersonation/support context.

**RM-AUDIT-EVENT-0003:** Action fields bind stable semantic action, request/command identity, target resource type/ID/generation and scope, before/after references or safe deltas, purpose, parameters classification, and effect/idempotency identity.

**RM-AUDIT-EVENT-0004:** Outcome distinguishes requested, allowed/denied, accepted, committed, completed, partially completed, canceled, failed, ambiguous, compensated, reversed, superseded, and unknown with reason/error and residuals.

**RM-AUDIT-EVENT-0005:** Event time, observed time, append time, effective period, monotonic/sequence evidence, clock source/quality/uncertainty, and time-zone/calendar context remain separate.

**RM-AUDIT-EVENT-0006:** Schema fields define required/optional/forbidden, type/unit/encoding, cardinality, classification, minimization, redaction/tokenization, normalization, unknown preservation, and compatibility.

**RM-AUDIT-EVENT-0007:** Secret values, credentials, private keys, authentication proofs, session tokens, raw payment instruments, unnecessary content, and unstable localized text are prohibited by schema rather than filtered only downstream.
