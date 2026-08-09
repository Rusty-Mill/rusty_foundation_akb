# PKI-validation cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | PKI-validation foundations 0.1.0; architecture model 1.95.0 |
| Accountable owner | PKI validation owner |
| Open blocking findings | None for dossier reviewability; PKI/cryptography/platform/privacy/accessibility specialist review, exact profiles/providers, executed corpora, and implementation evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | CERT/TRUST/PATH/VALIDATE/IDENTITY/STATUS/NETWORK/RESULT requirements | RFC and adversarial corpora, parser/resource fuzzing, alternate/cross-sign graph oracle, constraint/purpose/algorithm mutation, identity/IDN/wildcard corpus, hostile locator SSRF/recursion, cache rollback, override/pin and redaction review | trust result is context-bound evidence, not identity/authority; subjects/SANs/serials/locators/store contents/enterprise roots/exceptions may be sensitive |
| Performance | PKI-BENCH-0001–0006 | stage-separated parse/snapshot/build/validate/status/network/cache/concurrency/lifecycle runs with equivalent inputs/outcomes, hostile bounds, cold/warm and update storms | disabled validation/status/network or incomplete path search is not equivalent; no universal budget/native-performance claim exists |
| Accessibility | override/pin/network/status/product-consumer surfaces | keyboard/assistive-technology and spoofing review of certificate warnings, identity/purpose, exception scope/expiry, admin provenance, progress/cancel/offline/recovery and safe defaults | base validator need not display UI; inaccessible warning cannot authorize an exception, pin, trust mutation, identity change, or soft-fail policy |
| Internationalization | CERT-0006, IDENTITY-0001–0005, RESULT-0006 | exact profile-specific IDNA/Unicode/mailbox/URI rules, locale-independent comparison, bidi/control/confusable-safe presentation, original value preservation, localized explanations with stable codes | display equality is not security equality; generic Unicode normalization, locale/case folding, or DN/common-name matching is forbidden |
| Observability | RESULT-0002/0006, trust/network privacy | bounded stage/outcome/bound counters, digests and generation identifiers under policy, sanitized causal traces, redaction/cardinality/recursion review, subject/SAN/URL/serial/store/override canaries | validation artifacts can expose visited services, identities and enterprise policy; raw certificates/status objects are retained only under explicit evidence authority |
| Operations | TRUST-0007, STATUS-0007, RESULT-0004–0005, NETWORK requirements | trust/distrust/enterprise/user/pin updates, certificate/status expiry storms, clock/policy/provider changes, offline/proxy/captive/rollback, responder outage/compromise, cache loss, restart/shutdown/revalidation drills | absence of notification is not freshness; earliest material expiry and dependency generation govern reuse; emergency exceptions remain scoped and revocable |

**RM-PKI-QUALITY-0001:** Every trial or promotion review MUST bind all six quality dimensions to exact standards/profile, provider/platform/trust/network context, methods, accountable reviewers, findings, and affected claims.

**RM-PKI-QUALITY-0002:** Performance, UI, localization, diagnostics, and operations mechanisms MUST NOT weaken parsing/validation/status policy, broaden retrieval/trust/override authority, expose sensitive evidence, or collapse unknown/indeterminate outcomes.

**RM-PKI-QUALITY-0003:** Path construction, validation, identity matching, revocation/status, network/cache, proof-of-possession, and authorization evidence MUST remain separately observable in quality and failure reporting.

**RM-PKI-QUALITY-0004:** Trust/store/status/provider/clock/profile changes MUST trigger dependency-aware invalidation or revalidation; cache age or lack of a change event alone MUST NOT establish current validity.
