# ADR-0121: Safe transformation creates a new artifact generation with bounded claims

## Status

Accepted

## Context

Previewing, flattening, transcoding, macro removal, metadata stripping, content disarm and reconstruction, and canonical rewriting can reduce selected risks but may lose semantics or expose new parser behavior. Calling the output “the same file, now safe” obscures changed bytes, invalid signatures, inherited origin, tool vulnerabilities, consumer differentials, and threats outside the transformation profile.

## Decision

Rusty Mill models every security-relevant transformation as an immutable plan that produces a new artifact generation. The result binds source lineage, exact provider/profile, preserved/removed/substituted semantics, independent output validation, origin/quarantine propagation, integrity, and a threat-model- and consumer-scoped acceptance claim. Universal “sanitized” or “safe” claims are prohibited.

## Consequences

- Source evidence and signatures never silently transfer to derived bytes.
- Products can compare fidelity and risk reduction explicitly.
- Derived artifacts require independent storage, retention, policy, and cache identity.
- Some transformations will fail closed when unsupported structures or semantic preservation requirements cannot be reconciled.
