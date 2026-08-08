# Advisory and vulnerability model

**RM-REPOSITORY-ADVISORY-0001:** An advisory has stable provider-scoped identity, aliases, revision, state, title/summary/details, discovery/report/publication/update/withdrawal times, credits, weakness references, severity vectors, affected products, remediations, references, and signed provenance.

**RM-REPOSITORY-ADVISORY-0002:** Product identity uses exact ecosystem/namespace/package and, where needed, artifact/source/module/interface/configuration identities. Human product names do not drive matching.

**RM-REPOSITORY-ADVISORY-0003:** Affected, fixed, not affected, under investigation, last affected, and recommended states are separately asserted per product/version/architecture/platform/configuration. “Not affected” includes rationale and evidence.

**RM-REPOSITORY-ADVISORY-0004:** Version ranges use the target ecosystem's exact ordering and are supplemented by enumerated release or source-commit/artifact evidence where ambiguity exists. SemVer is not assumed for native or calendar/vendor versions.

**RM-REPOSITORY-ADVISORY-0005:** Severity records scheme/version/vector/score, assessor, environment assumptions, exploitability/evidence, scope, and time. Product deployment priority additionally depends on exposure, reachability, assets, mitigations, business impact, and update risk.

**RM-REPOSITORY-ADVISORY-0006:** Remediation distinguishes vendor fix, upgrade, configuration mitigation, workaround, containment, disable/yank/revoke, none available, and no fix planned with exact applicability, authority, side effects, and validation.

**RM-REPOSITORY-ADVISORY-0007:** Advisory revisions are immutable and monotonic. Corrections, new affected products, severity changes, exploit evidence, fixes, regressions, aliases, and withdrawal append a signed revision and change history rather than rewrite prior claims.

**RM-REPOSITORY-ADVISORY-0008:** Withdrawal preserves identity, prior revisions, time, authority, reason, replacement/duplicate relationship, and consumer guidance. It does not make the previous publication nonexistent.

**RM-REPOSITORY-ADVISORY-0009:** Machine-readable OSV/CSAF/CVE/ecosystem projections declare schema/profile version and loss. The authoritative Rusty Mill record does not infer unsupported semantics during conversion.

