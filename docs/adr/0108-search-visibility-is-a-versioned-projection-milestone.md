# ADR-0108: Search visibility is a versioned projection milestone

## Status

Accepted

## Context

Search engines often acknowledge indexing before a change is visible, make buffered segments visible before durable commit, and search replicas at different recovery points. A search index is also derived from source data through versioned schemas, analyzers, models, and authorization projections. Treating indexing success or refresh as source truth or complete durability creates stale, missing, resurrected, and unauthorized results.

## Decision

Rusty Mill models search-visible state as an immutable logical view over exact index/shard generations, source watermark, schema/analyzer/model/ranking and security policy generations. Source commit, capture, indexing, durability, replication, refresh visibility, and source convergence are distinct milestones. Search results state their view and partial/freshness evidence.

## Consequences

- Pagination and replay can bind point-in-time views.
- Products select explicit read-your-write or bounded-staleness contracts.
- Indexes remain rebuildable projections rather than sources of truth by default.
- Operational APIs cannot silently strengthen provider acknowledgment semantics.
