# Enrollment model and lifecycle

**RM-PKI-ENROLLMENT-0001:** An enrollment intent identifies operation kind, subject/principal/device/workload, requested certificate profile/purpose/identifiers, key generation/protection, target store/scope, issuer/policy, protocol, interaction, deadline, and authority ceiling.

**RM-PKI-ENROLLMENT-0002:** `initial`, `renew-same-key`, `rekey`, `modify`, `replace-lost`, `recover-archived`, `cross-certify`, `revoke`, and `status-only` are distinct operation kinds. Providers cannot substitute one silently.

**RM-PKI-ENROLLMENT-0003:** Enrollment progresses through immutable `intent`, `key-ready`, `request-built`, `submitted`, `pending`, `challenged`, `approved`, `issued`, `delivered`, `installed`, `activated`, `replaced`, `revoked`, `expired`, `rejected`, `cancelled`, `indeterminate`, and `recovery-required` evidence.

**RM-PKI-ENROLLMENT-0004:** An enrollment transaction binds request identifier, idempotency/replay state, protocol/server/account, policy/profile generations, key/public-key identity, authorization evidence, request bytes, requested and issued claims, response bytes, status, timestamps, and dependencies.

**RM-PKI-ENROLLMENT-0005:** Submission acceptance, authorization, issuance, delivery, store installation, private-key association, activation, and relying-party acceptance are separate milestones.

**RM-PKI-ENROLLMENT-0006:** Cancellation distinguishes not submitted, pending safely cancelled, authorization possibly consumed, issuance possibly occurred, certificate delivered, and installation/activation possibly changed. Ambiguous network outcomes reconcile by stable transaction/order identity.

**RM-PKI-ENROLLMENT-0007:** Retry reuses protocol-safe idempotency and reconciles existing requests/orders/certificates before creating new key or certificate generations. Duplicate issuance is reported, not hidden.

**RM-PKI-ENROLLMENT-0008:** Enrollment results retain all checks, providers, user/admin interaction, errors, pending/retry guidance, unknowns, expiries, and nonclaims; a boolean cannot erase lifecycle evidence.

