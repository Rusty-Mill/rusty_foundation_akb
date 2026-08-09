# ADR-0147: Readiness is an evidence bundle, not a label

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Document counts, clean links, planned conformance suites, and broad architecture coverage can look like completion while leaving semantics, assertion traceability, provider evidence, or benchmark baselines unproven.

## Decision

Every readiness claim binds a subject, scope, evidence frontier, dimension results, open findings, waivers, and review. Structural, definition, trial, provider, profile, release, and Stable-promotion readiness remain distinct. Unknown does not aggregate to pass.

## Alternatives considered

- A single completion percentage: rejected because it combines unlike scopes and hides blockers.
- Lifecycle status alone: rejected because Draft/Experimental/Stable does not identify which evidence exists.
- Reviewer judgment without a bound record: rejected because the conclusion cannot be reproduced or invalidated precisely.

## Consequences

- Progress reports become more candid and actionable.
- Promotion requires more explicit evidence bookkeeping.
- A domain can be definition-ready while correctly remaining Draft and implementation-ineligible.
