# PKI-issuance cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | PKI-issuance and CA-lifecycle foundations 0.1.0; architecture model 1.96.0 |
| Accountable owner | Certificate issuance owner |
| Open blocking findings | None for dossier reviewability; PKI/cryptography/CA operations/privacy/accessibility specialist review, exact protocols/providers/policies, executed evidence, and ceremonies remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | issuance requirements, CROSS-0001–0008 | hostile request/protocol corpus, POP/attestation replay/substitution, cross-tenant/profile/identifier escalation, serial/crash/restore, HSM/quorum/failover, CT/precertificate/status release, SSRF/redirect, secret/privacy canaries, compromise/recovery | request/POP/attestation are not authority; certificate issuance is not relying-party authorization; CA keys/ledger/publication are privileged independent boundaries |
| Performance | BENCH-0001–0006 | stage/end-to-end transaction matrix, protocol/provider differentials, fleet renewal/revocation load, CA/HSM/ledger/failover/recovery, sustained queue/fairness/outage runs | human/approval waits separate; incomplete proofing/status/CT/durability/audit/install/activation is not equivalent; no numeric budget/native-performance claim exists |
| Accessibility | CROSS-0005–0007 and interactive/admin surfaces | keyboard/assistive-technology and spoofing review of subject/requester/issuer/purpose/identifiers/key/store/publication, approval/quorum, progress/pending/cancel/recovery, emergency revocation and headless alternatives | inaccessible interaction cannot authorize broader claims, key export/escrow, public logging, CA action, exception, or ambiguous destructive recovery |
| Internationalization | names/identifiers/templates/errors/prompts | typed protocol/profile canonicalization, locale-independent security comparison, bidi/control/confusable-safe presentation, requested-versus-issued display, localized stable-code operations surfaces | display names/template labels are not identifiers or authority; implicit normalization/case/locale conversion cannot alter request, approval, policy, signed bytes, or transaction identity |
| Observability | CROSS-0003–0004/0008, ledger/audit | generation-linked intent/request/order/authz/issuance/certificate/store/service/renewal/revocation events, bounded metrics, redaction/cardinality/recursion review, secret/identifier/attestation canaries, audit completeness reconciliation | public CT/directory/status publication is explicit; raw identifiers, requests, keys, challenges, pending IDs, account/admin credentials and reusable artifacts are minimized |
| Operations | renewal/CA requirements | fleet deadline/outage/stampede/mass-revocation, root/intermediate/issuer/status/log rotation, serial/ledger backup/restore, cloned issuer, issuance halt, compromise, termination, store/service activation/rollback, recovery drills | issuance, distribution, activation, relying-party adoption, status propagation and old denial differ; restored executable/service state cannot roll credentials or ledger backward |

**RM-PKI-ISSUANCE-QUALITY-0001:** Every trial or promotion review MUST bind all six quality dimensions to exact protocol/profile/provider/platform/CA environment, methods, qualified accountable reviewers, findings, and affected claims.

**RM-PKI-ISSUANCE-QUALITY-0002:** Performance, UI, localization, diagnostics, and operations mechanisms MUST NOT weaken proofing/POP/policy/release controls, broaden authority/key exposure, leak sensitive/publication data, or collapse pending/indeterminate effects.

**RM-PKI-ISSUANCE-QUALITY-0003:** Request acceptance, authorization, issuance, ledger commit, CT/status prerequisites, delivery, installation, association, activation, health, renewal replacement, old denial, revocation/status propagation, and relying-party acceptance MUST remain separately observable.

**RM-PKI-ISSUANCE-QUALITY-0004:** CA continuity evidence MUST cover serial/transaction monotonicity, key/hierarchy generations, quorum/roles, active-clone prevention, trust/status/log distribution, compromise/issuance halt, recovery and termination without blanket audit/certification claims.
