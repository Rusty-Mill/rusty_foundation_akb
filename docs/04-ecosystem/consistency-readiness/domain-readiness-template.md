# Domain readiness review template

Copy sections into the conventional domain files. Replace every placeholder; `Pass` with placeholder or missing evidence is invalid.

## `cross-cutting.md`

| Field | Value |
|---|---|
| Review status | Unknown |
| Reviewed | YYYY-MM-DD |
| Review frontier | Domain and architecture generations |
| Accountable owner | Role; named assignee required for promotion |
| Open blocking findings | IDs or `None` with qualification |

| Dimension | Exact requirements | Planned/observed evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | | | |
| Performance | | | |
| Accessibility | | | |
| Internationalization | | | |
| Observability | | | |
| Operations | | | |

## `source-review.md`

| Field | Value |
|---|---|
| Review status | Unknown |
| Reviewed | YYYY-MM-DD |
| Expires | YYYY-MM-DD and/or material-change trigger |
| Reviewer | Role; named assignee required for promotion |
| Open blocking findings | IDs or `None` with qualification |

| Source | Class and reviewed status/version | Affected propositions | Impact and limitation |
|---|---|---|---|

## `ownership.md`

| Field | Value |
|---|---|
| Review status | Unknown |
| Reviewed | YYYY-MM-DD |
| Accountable owner | |
| Architecture reviewer | |
| Security reviewer | |
| Evidence reviewer | |
| Compatibility authority | |

### Ownership duties

### Bounded trial plan

Include exact hypotheses, platforms/providers, nonclaims, limits, stop conditions, evidence, cleanup, disposal, and the [trial template](../../05-governance/implementation-trials/trial-template.md).

## `promotion-review.md`

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Exact domain/capability generation |
| Architecture | Exact model generation |
| Proposed decision | |
| Implementation authority | None |

### Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|

### Decision boundary

For acceptance add named accountable people, reviewers and independence, decision date, exact scope, findings/waivers, open-question dispositions, and trial constraints. Acceptance changes maturity only; it does not authorize code.

