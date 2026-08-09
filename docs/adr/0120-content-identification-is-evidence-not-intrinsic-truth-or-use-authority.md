# ADR-0120: Content identification is evidence, not intrinsic truth or use authority

## Status

Accepted

## Context

Content can carry a protocol media type, filename extension, platform type, magic signature, container identity, parser-valid structure, embedded active content, and multiple polyglot interpretations. Platform registries and detectors use different rule sets and purposes. Collapsing them into one “true type” lets an attacker route bytes through a less-privileged interpretation and tempts callers to treat recognition as permission to preview, import, open, or execute.

## Decision

Rusty Mill represents each declaration, association, detection, structural validation, parser interpretation, and conflict as scoped versioned evidence. Identification results never grant use authority. Purpose-specific policy evaluates all credible interpretations plus origin, trust, malware/reputation, resource, and user/admin context before selecting an action.

## Consequences

- Ambiguous and polyglot content remains representable instead of arbitrarily classified.
- Applications can explain why declarations and detections disagree.
- Callers must select candidate sets, evidence thresholds, and downstream consumer scope.
- Convenience providers may expose a preferred display label but cannot erase underlying evidence or nonclaims.
