# Capability dependency graph model

**Status:** Draft

The graph is a versioned architectural artifact derived from capability specifications. It supports review, profile resolution, impact analysis, documentation generation, and verification planning. It is not a runtime service design.

## Nodes

Each node records a stable capability identifier, contract version, maturity, domain, owner, and specification link. Profiles and services may be represented in separate views but are not capability nodes.

## Edges

- `requires`: the source cannot satisfy its minimum contract without the target.
- `optionally-uses`: the source can improve quality or add optional behavior when the target is present.
- `conflicts-with`: the two capabilities or specified versions cannot be selected together under stated conditions.

Edges may carry a version constraint, condition, rationale, and requirement identifier. OS names and crate names are prohibited as dependency targets.

## Invariants

- The directed `requires` subgraph is acyclic.
- Every edge appears in the source capability specification.
- A required edge points to the narrowest sufficient capability.
- Optional edges cannot change the source's minimum guarantees silently.
- Conflict edges explain whether the conflict is semantic, authority-related, resource-related, or transitional.
- Profile resolution either produces a satisfiable graph or a diagnostic explaining each unsatisfied constraint.

## Views

- Domain view: internal cohesion and candidate boundaries.
- Profile view: transitive requirements for a workload.
- Authority view: sensitive capability paths and privilege concentration.
- Platform view: native, emulated, degraded, and unavailable nodes.
- Change-impact view: downstream contracts, profiles, tests, and releases affected by a proposal.

## Serialization direction

A future machine-readable representation should be deterministic, reviewable as text, schema-versioned, and losslessly linked to Markdown specifications. The choice of YAML, TOML, JSON, or generated metadata remains open pending toolchain experiments; RFC-0001 does not commit to a syntax.
