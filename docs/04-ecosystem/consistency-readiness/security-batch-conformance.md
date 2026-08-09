# Security-foundation batch conformance specification

**Status:** Planned composed evidence; no run authorization  
**Authority:** [Security batch integration review](security-batch-integration-review.md)

| Family | Composed units | Required oracle |
|---|---|---|
| `SEC-BATCH-CONF-001` identity/authority confusion | authority, secrets, crypto, validation, issuance | equal labels, accounts, key possession, certificate subject/SAN, trust result, entitlement, or audit record never grant unrelated resource authority |
| `SEC-BATCH-CONF-002` pre-side-effect selection | all seven | individually mutate every policy/provider/generation/constraint after planning; stale or mismatched plan fails before affected provider activation, key creation, child release, store mutation, retrieval, signing, or issuance |
| `SEC-BATCH-CONF-003` random consumer boundary | random, secrets, crypto, issuance | exact-fill/failure and no-output leakage hold while purpose-specific nonce/salt/key/request rules remain consumer-owned; no statistical result certifies composition |
| `SEC-BATCH-CONF-004` opaque secret/key composition | authority, secrets, crypto | non-reveal operations remain provider-mediated; handles/references cannot be exported, substituted, confused across tenants/providers, or used for undeclared operations |
| `SEC-BATCH-CONF-005` crypto/validation separation | crypto, validation | valid signatures with invalid syntax/path/purpose/identity/time/status fail at the correct stage; a validation result retains exact algorithm/provider and trust context |
| `SEC-BATCH-CONF-006` validation/issuance separation | authority, crypto, validation, issuance | POP/request/attestation/validation cannot authorize copied claims; issued/delivered/installed/active/trusted/authorized remain distinct |
| `SEC-BATCH-CONF-007` restricted release barrier | authority, restricted execution, secrets | required authority/protection/control mismatch or unknown prevents application-controlled code; failure/cancellation leaves no unrestricted child or leaked authority/secret |
| `SEC-BATCH-CONF-008` downgrade/substitution | all seven | unsupported algorithm, provider, control, protection, trust/status policy, enrollment profile, or authority constraint never triggers silent fallback or “best available” substitution |
| `SEC-BATCH-CONF-009` cancellation/indeterminate | restricted execution, secrets, crypto, validation, issuance | fault at every accepted/native/remote/durable boundary preserves truthful outcome, ownership, residuals, and reconciliation; timeout never fabricates rollback |
| `SEC-BATCH-CONF-010` generation invalidation | all seven | policy, authority, secret, key, provider, trust, status, certificate, account/session, clock, sandbox, and platform changes invalidate only correctly scoped dependent evidence and never remain silently cached |
| `SEC-BATCH-CONF-011` revocation and rotation | authority, secrets, crypto, validation, issuance | successor creation/use, predecessor denial, alias/cache/replica/status propagation, in-flight work, committed effects, partitions, and recovery are independently observed |
| `SEC-BATCH-CONF-012` disclosure isolation | all seven | canaries are absent from errors, prompts, accessibility state, logs, traces, metrics, crash artifacts, reports, and benchmark output across correlated operations |
| `SEC-BATCH-CONF-013` provider sharing | secrets, crypto, validation, issuance | a shared store/library/service/HSM exposes only separately selected operations and claims; failure, certification, update, backup, or deletion evidence does not transfer between units |
| `SEC-BATCH-CONF-014` sync/async boundary | all seven | local sync paths do not create runtimes or pump loops; remote/interactive/network/provider waits expose bounded async lifecycle, deadlines, cancellation, and no hidden I/O |
| `SEC-BATCH-CONF-015` restore/update recovery | all seven | snapshot/restore, rollback, provider update, trust update, CA recovery, and process restart preserve generation monotonicity or explicitly invalidate and reconcile every dependent artifact |

Each case binds exact unit contract versions, platform/provider artifacts and configuration, profile/consumer policy, authority, inputs and generations, topology, clocks, failure schedule, expected per-stage outcomes, disclosure policy, cleanup inventory, and reproducible evidence provenance.

**RM-SECURITY-BATCH-CONFORMANCE-0001:** Passing unit suites independently MUST NOT count as batch conformance; every claimed composition MUST execute the applicable cross-unit families above.

**RM-SECURITY-BATCH-CONFORMANCE-0002:** A failed earlier stage MUST prove that prohibited later provider activations and effects did not occur, or report an explicit indeterminate state and reconciliation requirement.

**RM-SECURITY-BATCH-CONFORMANCE-0003:** Differential testing MUST compare guarantee-equivalent Windows, Linux, and macOS compositions while preserving provider-specific mechanisms, unsupported states, and nonclaims.

**RM-SECURITY-BATCH-CONFORMANCE-0004:** Reports MUST preserve unit-specific assertion identities and raw sanitized evidence; a batch pass/fail summary MUST NOT erase partial, unknown, waived, or consumer-qualified results.

**RM-SECURITY-BATCH-CONFORMANCE-0005:** This specification defines evidence only and MUST NOT authorize native/unsafe code, provider access, production identities/keys/certificates/policies/stores, external load, or implementation.
