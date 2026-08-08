# Profile resolution report

**Status:** Draft evidence schema

## Purpose

The report is the auditable boundary between requested workload semantics and the providers a deployment will actually use. It is immutable, machine-serializable in the future, and renderable as Markdown/JSON without making either format authoritative yet.

## Required sections

| Section | Contents |
|---|---|
| Request | Profile identity/version, request digest, timestamp source, deployment facts, policy identity/version |
| Authority | Sanitized authority summary and unsatisfied authority constraints; never credentials or secret material |
| Catalog | Provider identities/versions/artifact digests and evidence-set digests considered |
| Expansion | Direct and transitive required, conditional, optional, and prohibited members |
| Evaluation | Per-constraint expected value, observed value, evidence reference, freshness, and outcome |
| Selection | Exact providers, contract versions, quality/protection claims, service compositions, and tie-break rationale |
| Disclosures | Emulation, accepted degradation, interaction, ambient inputs, residual assumptions, optional absence |
| Failure | Structured minimal unsatisfied causes, rejected candidates, and safe remediation classes |

## Outcome

The top-level outcome is `satisfied` or `unsatisfied`; there is no partial success. A satisfied report may contain explicitly permitted degradation. An unsatisfied report does not return a usable partial provider set unless a separate diagnostic API requests candidates with no execution authority.

## Integrity and privacy

Reports bind to evidence and provider artifact digests. Signing is a delivery/evidence policy, not assumed by the schema. Reports redact secret values, native credentials, sensitive paths, personal identifiers, and provider-internal policy details by default. A redacted report states which fields were omitted and why.

## Conformance assertions

- Reordering the provider catalog cannot change selection except through the declared tie-break rule.
- Every selected claim links to fresh evidence with matching platform and configuration scope.
- Each rejection identifies at least one exact failed constraint.
- No required or prohibited transitive member is absent from evaluation.
- Report replay with identical inputs yields the same result and selection digest.
- Changing any material input changes the request or selection digest.

