# Authority cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Scope | Authority, policy, attenuation, delegation, provenance, enforcement, transfer, expiry, revocation, and audit planning |
| Open blocking findings | None for dossier reviewability; implementations, providers, profiles, qualified reviewers, and executed evidence do not exist |

| Dimension | Required treatment | Evidence boundary |
|---|---|---|
| Security | explicit least authority, confused-deputy resistance, monotonic derivation, authenticated audience-bound transfer, replay/use/depth bounds, fail-closed unknowns, operation-time enforcement, alias-aware revocation | claims are scoped vectors tied to exact mechanisms and adversarial probes, never a scalar security level |
| Performance | separate policy evaluation/cache, native check, operation, derivation, transfer protocol, revocation propagation, audit, and reconciliation costs | faster results are comparable only with identical freshness, enforcement, failure, disclosure, and lifecycle semantics |
| Accessibility | policy explanations and consent/approval interactions expose semantic purpose, affected resource/action, consequences, duration, alternatives, progress, cancellation, and recovery through accessible channels | accessibility does not reveal secret inputs or turn UI confirmation into authority |
| Internationalization | identifiers remain typed native values; human labels and explanations use explicit locale, stable machine reason codes, bidi-safe presentation, and non-lossy diagnostics | localized/display equality never drives authority comparison or policy keys |
| Observability | correlate request, decision, enforcement, effect, delegation, invalidation, and reconciliation with redaction and retention policy | audit events are evidence, not domain truth, complete capture proof, bearer authority, or a replacement for native outcomes |
| Operability | inventory authorities/aliases/generations, invalidate caches, stop delegation, rotate policy, reconcile ambiguous transfer, propagate revocation, recover providers, and account for residual effects | emergency actions require explicit authority, dual control where selected, rollback/forward recovery, and post-event evidence |

**RM-SECURITY-AUTHORITY-QUALITY-0001:** Every claimed authority guarantee MUST name its security, performance, accessibility, internationalization, observability, and operability method or an explicit nonclaim.

**RM-SECURITY-AUTHORITY-QUALITY-0002:** Redaction MUST preserve stable semantic reason/evidence categories while enforcing disclosure authority and preventing credential, bearer, secret-policy, sensitive-name, or cross-tenant leakage.

**RM-SECURITY-AUTHORITY-QUALITY-0003:** Interactive consent, accessibility state, localized labels, logs, traces, dashboards, and operator controls MUST NOT become hidden grants, enforcement points, or authority-transfer channels.

**RM-SECURITY-AUTHORITY-QUALITY-0004:** Performance and availability claims MUST include policy/evidence freshness, native enforcement, delegation/revocation topology, audit/reconciliation cost, failure behavior, and residual limitations.
