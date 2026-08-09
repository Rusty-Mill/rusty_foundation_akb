# RFC-0002: Implementation trial governance

**Status:** Accepted  
**Authors:** Rusty Mill maintainers  
**Reviewers:** Architecture, capability, security, standards, and evidence review  
**Created:** 2026-08-08

## Summary

Adopt a generation-bound lifecycle and reusable record for bounded implementation trials. Experimental capability promotion, standards-profile compliance, and exact trial authorization are separate conjunctive gates. Trial results are evidence rather than architectural precedent.

## Motivation

The specification-first boundary needs a controlled way to learn from native implementations without allowing prototypes, repository structure, provider choices, or convenient APIs to become implicit architecture.

## Goals and non-goals

Goals are auditable authorization, falsifiable learning, cross-platform provider evidence, material-drift handling, safe isolation, and outcome-neutral closeout. This RFC does not select a trial subject, authorize code, choose a metadata serialization, establish a crate layout, or permit a release.

## Proposed design

Use the [implementation trial governance model](../05-governance/implementation-trials/README.md) and its template. A proposed trial passes explicit entry review, operates only within bound generations and limits, pauses on material drift, and closes as successful, failed, inconclusive, or terminated. Follow-on architecture, maturity, reuse, and release decisions use their ordinary governance paths.

## Behavioral contract impact

No capability semantics change. Trial observations may propose later changes but cannot amend contracts directly.

## Capability graph and profile impact

No graph or capability profile changes. Each trial binds exact graph/profile inputs and records drift.

## Platform behavior and variance

Trials declare exact Windows, Linux, and macOS frontiers and native-provider mappings. Missing evidence remains unknown; variance is preserved rather than hidden.

## Security, performance, accessibility, i18n, and observability

Each quality has an applicability decision, method, findings, and limitations. Authority, unsafe/FFI, secrets, privileged runners, provenance, comparability, accessibility, localization, telemetry loss, and privacy are explicit gates.

## Compatibility, versioning, packaging, and migration

Trial interfaces and artifacts are experimental and non-release. The authorization binds generations and expires or pauses on material drift. Reuse requires separate review.

## Conformance and benchmarks

Plans bind requirements to semantic assertions, executable cases, benchmark scenarios, environments, attempts/runs, raw evidence, and provenance before implementation begins.

## Alternatives considered

- Allow Experimental maturity alone: rejected because it omits repository, evidence, operational, and scope controls.
- Treat a trial RFC as future implementation precedent: rejected because learning frequently changes boundaries.
- Require a permanent repository layout and metadata encoding now: deferred until at least two materially different trials expose real needs.
- Prohibit implementation until Stable: rejected because native evidence is needed to learn whether Draft contracts can advance.

## Drawbacks and risks

The process adds review cost and can slow experiments. Tight templates can encourage checkbox compliance. Falsifiable questions, exact evidence links, scoped reviewers, and outcome-neutral closeout constrain those risks.

## Unresolved questions

The first implementation RFC will propose standards-profile serialization and enforcement only after at least two materially different repository trials. No trial candidate is selected by this RFC.

## Rollout and lifecycle

The model is effective immediately. Existing prototypes cannot claim authorization retroactively; they may supply clearly qualified input evidence. Changes use a superseding RFC when semantics materially change.

