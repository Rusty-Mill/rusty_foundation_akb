# RFC-0001: Capability specification system

**Status:** Draft  
**Authors:** Rusty Mill founders  
**Reviewers:** Unassigned  
**Created:** 2026-08-08

## Summary

Establish the minimum human-readable model for capability identity, specification, dependency graphs, normative requirements, profiles, and evidence traceability. Defer machine-readable syntax and Rust API design until the model has been exercised on a vertical slice.

## Motivation

“Abstract capabilities, not operating systems” needs a repeatable specification system. Without one, domains will choose inconsistent boundaries, requirements will be difficult to verify, and platform variance may leak into public APIs.

## Goals and non-goals

### Goals

- Give every capability and normative requirement a stable identity.
- Standardize domain analysis and capability documents.
- Define dependency semantics and graph invariants.
- Connect contracts to profiles, conformance, benchmarks, and releases.
- Support human review before selecting serialization or code-generation tools.

### Non-goals

- Define Rust traits, types, crates, or workspaces.
- Choose a metadata serialization format.
- Design runtime provider discovery or dependency injection.
- Finalize the first production capability taxonomy.

## Proposed design

1. Capability identifiers follow `rm.<domain>.<capability>` and name behavior rather than implementation.
2. Contracts use SemVer independently of their stable identifier.
3. Normative requirements use stable `RM-<DOMAIN>-<CAPABILITY>-<NNNN>` identifiers.
4. Every specification follows the common capability template.
5. Dependency edges are limited initially to `requires`, `optionally-uses`, and `conflicts-with`.
6. The required-dependency graph must be acyclic.
7. Human-readable Markdown remains normative during the foundation phase.
8. Traceability links requirements to decisions, conformance assertions, benchmarks, provider evidence, profiles, and releases.

## Behavioral contract impact

This RFC standardizes the container and identity system for contracts. It does not accept any individual capability contract.

## Capability graph and profile impact

Profiles resolve against versioned capability nodes and their transitive required dependencies. Optional dependencies cannot silently strengthen a profile's minimum guarantees.

## Platform behavior and variance

Every capability specification includes a Windows, Linux, and macOS realization matrix using native, emulated, degraded, unavailable, or unknown states. This matrix documents research and does not itself constitute conformance.

## Security, performance, accessibility, i18n, and observability

The template makes each dimension an explicit review section. Authors must provide requirements or a reviewable explanation of non-applicability.

## Compatibility, versioning, packaging, and migration

The specification format begins at version 1 when accepted. Capability contracts use SemVer; requirement identifiers are never reassigned. A future metadata format must migrate without changing semantic identity.

## Conformance and benchmarks

Every normative **MUST** maps to an assertion or documented evidence method. Every performance claim maps to a benchmark plan with a native baseline. Tooling is deliberately deferred.

## Alternatives considered

### API-first specifications

Rejected because Rust syntax would freeze boundaries before cross-platform semantics are understood.

### Machine-readable schema first

Deferred because choosing a schema before exercising the information model encourages tool-driven omissions and premature code generation.

### Free-form domain documents

Rejected because cross-domain review, graph validation, and conformance traceability would remain inconsistent.

## Drawbacks and risks

- Structured authoring adds overhead before implementation.
- Identifier schemes may need refinement after the first domain slice.
- Manual traceability can drift until validation tooling exists.
- Overly broad capabilities may still pass template review without careful scenario analysis.

## Unresolved questions

- Which domain should supply the reference vertical slice?
- When should the metadata schema become machine-readable?
- Should requirement identifiers encode domain aliases permanently or use opaque numbers?
- What minimum evidence is necessary for Experimental maturity?

## Rollout and lifecycle

1. Review this RFC and the companion templates.
2. Exercise them on one small but cross-cutting domain slice.
3. Revise based on friction and missing information.
4. Accept the RFC before creating stable capability specifications.
5. Propose serialization and validation tooling separately after two real specifications exist.

## Trial application

The model is now being exercised by the [runtime and time vertical slice](../02-capabilities/runtime-time/README.md). Its documents remain Draft and provide feedback to this RFC; they do not imply that RFC-0001 has been accepted.
