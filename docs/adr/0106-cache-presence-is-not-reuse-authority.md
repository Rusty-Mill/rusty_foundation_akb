# ADR-0106: Cache presence is not reuse authority

## Status

Accepted

## Context

A cache can physically contain an entry that is stale, invalidated, corrupt, for another tenant or representation, produced by an obsolete configuration, or no longer authorized. Treating presence or a key match as a valid hit creates privacy, correctness, and security failures.

## Decision

Rusty Mill authorizes reuse only after evaluating canonical key and representation identity, privacy partition, entry/configuration generation, integrity, freshness/validation policy, invalidation epoch, request context, and current authorization. Lookup reports distinguish candidate presence from authorized reuse.

## Consequences

- Cache APIs return evidence-rich outcomes rather than only optional values.
- Policy and authorization can reject physically present entries.
- Cache keys and partitions are architectural contracts.
- Providers may optimize evaluation but cannot weaken the selected policy.
