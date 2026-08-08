# ADR-0042: Address reservation is not memory commitment

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows exposes explicit reserve/commit, while Unix-like mappings interact with demand paging and overcommit. Across all systems, obtaining an address range does not prove resident physical pages, future fault success, or durable backing.

## Decision

The portable region model separates address reservation, backing/commit quality, accessibility, residency, locking, and durability. Providers publish exact state transitions and accounting evidence instead of normalizing them to a single allocated/not-allocated boolean.

## Consequences

- Workloads can negotiate truthful address-space and backing guarantees.
- Out-of-memory/fault behavior remains platform-policy dependent and testable.
- Higher-level allocators must state which stage their success actually establishes.

