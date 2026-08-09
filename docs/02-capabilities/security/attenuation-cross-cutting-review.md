# Authority-attenuation cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | `rm.security.attenuate` 0.1.0; architecture model 1.90.0 |
| Accountable owner | Authority-attenuation capability owner |
| Open blocking findings | None for capability planning eligibility; authority-kind, native-enforcement, deployment, revocation, specialist, and implementation evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | ATTENUATE-0001–0010, A-claim model | multidimensional subset property tests, ambient-grant probes, native alias/bypass adversaries, transfer/revocation races, credential/policy canaries | A-label is not a scalar security score; logical narrowing may coexist with native bypasses; restricted execution is separately composed |
| Performance | ATTENUATE-BENCH-0001–0005 | equivalent derive/inspect/concurrent lifecycle/transfer/revocation scenarios with subset, enforcement-vector, leak, and reconciliation gates | no numeric budget or native-performance claim exists; weaker constraints/enforcement are non-equivalent baselines |
| Accessibility | effective-constraint, consent/transfer, denial, expiry/revocation consumer surfaces | keyboard/assistive-technology review, stable nonsecret summaries, clear denial/expiry/revocation status, accessible recovery without broadening authority | capability owns no UI; products must not hide consequential attenuation or suggest that advisory/native states are equivalent |
| Internationalization | identifiers/summaries/provenance and policy diagnostics | locale-independent authority identity/constraint evaluation, bidi/control-safe labels, localized explanations separated from canonical constraints | localized/display identifiers are not authority identity; translation cannot change constraints, audience, lifetime, or delegation depth |
| Observability | ATTENUATE-0004–0005/0010 | structured nonsecret lineage/claim vectors, derivation/transfer/revoke correlations, redaction/cardinality/recursion review, native denial correlation | logs are evidence, not authority or enforcement; credentials, handles, secret policy inputs, and sensitive resource names remain protected |
| Operations | ATTENUATE-0006–0009, transfer/revocation composition | parent/child close, alias inventories, expiration, transfer reject/cancel, revocation latency/survivors, provider restart, policy/native drift, reconciliation drills | exact revocation delivery/object lifetime, alias control, deployment assumptions, incident handling, and operator runbooks remain product/provider inputs |

**RM-SECURITY-ATTENUATE-QUALITY-0001:** Every trial MUST bind all quality dimensions to exact authority kinds, constraint dimensions, native mechanisms, deployment contexts, owners, findings, and affected claims.

**RM-SECURITY-ATTENUATE-QUALITY-0002:** Portable subset proof, native enforcement, isolated context, defense-in-depth evidence, transfer, revocation, and restricted-execution verification MUST remain separate claims.

**RM-SECURITY-ATTENUATE-QUALITY-0003:** Accessibility, localization, and observability surfaces MUST explain constraints without becoming authority, broadening rights, or disclosing credential/secret policy material.
