# ADR-0162: Attenuation enforcement is a scoped claim vector, not a security score

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

Authority attenuation spans operation, resource, lifetime, audience, delegation depth, native enforcement, isolated context, independent controls, aliases, transfer, revocation, and bypass assumptions. The A0–A3 shorthand helps name common evidence patterns, but platform mechanisms cover different dimensions and deployment assumptions. Reading a higher label as universally stronger can conceal a missing constraint, ambient bypass, uncontrolled alias, or weaker lifecycle guarantee.

## Decision

Every attenuation result reports a scoped enforcement claim vector. The A0–A3 label is a summary derived from that vector and its evidence, never a scalar security score or substitute for multidimensional subset proof. Comparisons and profile requirements bind exact dimensions, mechanisms, aliases, bypass assumptions, deployment context, lifecycle, transfer, and revocation semantics.

No A-level authorizes elevation, authenticates a principal, proves sandbox containment, eliminates native aliases, or guarantees universal revocation. Restricted execution separately composes and verifies pre-execution controls.

## Options considered

- Treat A0–A3 as a total security ordering: simple but hides incomparable dimensions and deployment assumptions.
- Remove all summary labels: precise but makes recurring provider evidence harder to communicate.
- Retain labels as evidence-vector summaries: compact while preserving exact claims and nonclaims.

## Consequences

- Conformance reports and benchmarks record complete claim vectors and bypass probes.
- Profiles cannot request “A2” without naming required dimensions and context.
- Provider mechanisms with different vectors remain incomparable rather than coerced into one score.
- Promotion claims bind exact authority kinds and native contexts.

## Verification

The [attenuation traceability](../02-capabilities/security/attenuation-traceability.md), [quality review](../02-capabilities/security/attenuation-cross-cutting-review.md), and [source review](../02-capabilities/security/attenuation-source-review.md) require exact claim-vector evidence and prohibit scalar inference.
