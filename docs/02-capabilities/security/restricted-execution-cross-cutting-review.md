# Restricted-execution cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | restricted-execution contract 0.1.0; architecture model 1.92.0 |
| Accountable owner | Restricted-execution owner |
| Open blocking findings | None for dossier reviewability; native composition, specialist review, executed evidence, and production threat model remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | RESTRICTED-0001–0010, threat model | pre-release execution oracle, allowlist/ambient-authority probes, constraint bypass matrix, degradation-policy mutation, supervisor/adversarial-child failures, secret canaries | no portable sandbox-strength scalar; compromised kernel and native aliases outside the composition remain deployment assumptions |
| Performance | RESTRICTED-BENCH-0001–0005 | stage-separated cold/warm launch, readiness, lifecycle, failure/cancel/reconciliation, equivalent native baseline | security stages cannot be omitted or pre-applied asymmetrically; no numeric budget/native-performance claim exists |
| Accessibility | RESTRICTED-0002, 0006–0008 | selecting-product review of consent/policy failure, degradation disclosure, progress, cancellation, readiness, recovery, and headless behavior | base service has no mandatory UI; inaccessible consent cannot authorize degradation or authority transfer |
| Internationalization | manifest diagnostics and audit | stable machine codes, locale-independent policy evaluation, bidi/control-safe labels, localized product explanations with invariant evidence identifiers | localized text cannot participate in executable/resource/identity comparison or manifest digest semantics |
| Observability | RESTRICTED-0006, 0010 | stage/result counters, bounded causal traces, policy/evidence identifiers, redaction/cardinality/recursion review, child-input and credential canaries | arguments, environment, credentials, authority material, child output, and sensitive paths/addresses are excluded unless separately authorized |
| Operations | RESTRICTED-0007–0009 | supervisor crash/kill, orphan/descendant, reboot/session/logout, resource pressure, policy/provider update, cleanup/reconciliation drills | host/container/service-manager and packaging context materially change claims; unsupported lifecycle states must remain explicit |

**RM-SECURITY-RESTRICTED-QUALITY-0001:** Every trial or promotion review MUST bind all six quality dimensions to exact manifest/provider/platform methods, accountable reviewers, findings, and affected claims.

**RM-SECURITY-RESTRICTED-QUALITY-0002:** Security or performance evidence MUST NOT collapse creation, restriction, verification, release, readiness, supervision, termination, reaping, and cleanup into one launch duration or success flag.

**RM-SECURITY-RESTRICTED-QUALITY-0003:** Accessibility, localization, diagnostics, and operator controls MUST NOT broaden authority, authorize degradation implicitly, alter policy comparison, or disclose sensitive manifest/child data.

**RM-SECURITY-RESTRICTED-QUALITY-0004:** A native mechanism, sandbox label, container state, process owner, or successful child exit MUST NOT substitute for adversarial verification of the complete promised composition.
