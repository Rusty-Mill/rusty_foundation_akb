# ADR-0132: Secret rotation completes at successor use and predecessor denial

## Status

Accepted

## Context

Secret managers commonly report rotation after generating or storing a new value. Dependents may still use the predecessor, may not have reloaded successfully, or may have received an incompatible bundle. The target may continue accepting the old credential indefinitely. Treating issuance as completion creates both outage and compromise risk.

## Decision

Rusty Mill models rotation as a staged reconciliation. Completion requires evidence that selected dependents have authenticated or performed the intended operation with the successor, the normal issue path selects it, and the target denies the predecessor within the declared boundary. Unavailable dependents, targets, offline copies, and unverifiable denial remain explicit residuals.

## Consequences

- Rotation integrates deployment health with target-side credential state.
- Overlap is explicit and bounded rather than accidental.
- Emergency compromise rotation cannot roll back to the compromised predecessor.
- Reports distinguish generation, distribution, adoption, revocation, denial, and residual milestones.
