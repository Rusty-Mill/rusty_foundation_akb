# ADR-0155: Development standards are implementation entry gates

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Domain promotion alone does not define how implementation code, unsafe/native boundaries, dependencies, tests, CI, reviews, or release evidence must be produced. Allowing each first trial to invent its own practice would create precedent before governance exists.

## Decision

Foundation software-development standards are a separate conjunctive entry gate for every implementation trial. Domain Experimental authorization and an applicable repository standards profile are both required. Standards govern development evidence but cannot invent capability semantics or implementation authority.

## Alternatives considered

- Let initial repositories establish conventions organically: rejected because early accidents would harden into ecosystem precedent.
- Put all rules in each domain specification: rejected because cross-cutting engineering rules would duplicate and drift.
- Defer standards until Stable release: rejected because unsafe, dependency, testing, and API debt would already exist.

## Consequences

- No implementation trial is authorized merely because its domain scorecard passes.
- Repositories inherit one coherent baseline and may strengthen it locally.
- Exceptions are visible and cannot silently redefine architecture or release claims.
