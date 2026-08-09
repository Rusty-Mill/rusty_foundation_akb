# ADR-0122: Sensitivity labels are scoped assertions, not protection or authority

## Status

Accepted

## Context

Organizations define different label vocabularies, dimensions, legal meanings, and orderings. Labels may be applied manually, by defaults, inference, inheritance, services, or import mappings. Some products couple a label to markings, encryption, rights, retention, or DLP, but those effects can fail, lag, differ by application, or be removed independently. Treating a label as intrinsic truth or completed protection creates unsafe authorization and audit conclusions.

## Decision

Rusty Mill models each sensitivity label as an issuer-, taxonomy-, revision-, subject-generation-, method-, evidence-, and time-scoped assertion. Classification, policy decision, marking, encryption, rights publication, retention, channel enforcement, and downstream observation remain separate milestones and evidence. Labels can influence policy but never grant authority or prove an effect by themselves.

## Consequences

- Foreign and conflicting labels remain representable and require explicit mappings.
- Products can reconcile metadata, markings, encryption, rights, and DLP independently.
- Every use decision names the label and policy generations it relied upon.
- Convenience integrations may orchestrate effects but must expose partial completion and nonclaims.
