# ADR-0163: Maturity promotion units follow evidence boundaries, not directory layout

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

The readiness model initially treated one capability directory as one maturity subject. Most early directories were cohesive. The security directory now contains authority semantics, restricted execution, secure randomness, native secret protection, cryptography/key management, PKI validation, and certificate issuance. These subjects share vocabulary and compose, but have different owners, specialist reviewers, standards/providers, compatibility surfaces, conformance suites, operational risk, release cadence, and trial boundaries.

A single security promotion decision would either block small foundational capabilities on unrelated PKI/CA work or allow partial evidence to imply maturity across high-risk surfaces. Moving files into new directories merely to satisfy tooling would confuse governance with documentation topology and prematurely suggest crate/repository boundaries.

## Decision

Define maturity promotion units by coherent ownership, evidence, compatibility, risk, and release boundaries. A directory may contain multiple units, and a unit may cite shared evidence. Composite directories publish an authoritative `promotion-units.md` registry with stable identities, Draft/Experimental/Stable state, accountable roles, primary specifications, and scope summaries.

Unit decisions are independent and conjunctive. Shared evidence is proposition-scoped and never transfers maturity implicitly. Directory-level maturity is an aggregate view, not a separate shortcut. Documentation location, crate/workspace boundaries, repositories, packages, and implementation topology remain separate decisions.

## Options considered

- One directory equals one promotion unit: simple tooling but false governance for composite domains.
- Reorganize files immediately into directories per unit: aligns current tooling but creates disruptive and premature topology decisions.
- Govern explicit units independent of location: accurate maturity boundaries with stable links and incremental migration.

## Consequences

- Readiness tooling indexes explicit unit registries in addition to directory domains.
- Existing directory scorecards remain useful aggregate/backlog views but cannot hide child-unit state.
- Capability-level dossiers can mature incrementally without promoting unrelated siblings.
- Later documentation moves may improve navigation but require no maturity reset if identities and evidence remain stable.
- Units cannot be split merely to inflate percentages; reviews must document the forcing functions.

## Verification

The [promotion-unit model](../04-ecosystem/consistency-readiness/promotion-unit-model.md), [security registry](../02-capabilities/security/promotion-units.md), and audit generator validate stable unit identities and primary source existence while preserving nonauthorization.
