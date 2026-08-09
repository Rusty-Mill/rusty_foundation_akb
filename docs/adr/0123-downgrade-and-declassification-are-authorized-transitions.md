# ADR-0123: Downgrade and declassification are authorized transitions

## Status

Accepted

## Context

Changing a label to a less restrictive value may broaden recipients, remove markings or encryption, weaken retention or channel policy, and propagate to many copies and services. A metadata edit or successful redaction does not establish authority, complete downstream reconciliation, or reverse prior disclosure. Automated classifiers and users can also be wrong, but correction must not become a bypass.

## Decision

Rusty Mill models downgrade, declassification, label removal, protection removal, recipient broadening, and weaker cross-taxonomy mapping as distinct immutable transition plans. Each binds current subject and policy generations, requester/approver authority, structured reason, required evidence and transformation, independent validation, conditional commit, downstream reconciliation, audit, and residuals.

## Consequences

- Background classifiers cannot silently lower an effective handling state.
- False-positive correction and appeal remain supported through governed evidence.
- Partial removal or propagation is visible and retains the safer effective policy where required.
- Prior disclosure cannot be described as rolled back; response and reconciliation are separate effects.
