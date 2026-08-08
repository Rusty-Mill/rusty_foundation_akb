# ADR-0046: Scheduling controls are scoped requests, not execution guarantees

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows priority/group affinity, POSIX schedulers/cpuset affinity, and Apple QoS use different policy, privilege, topology, and dynamic adjustment models. Numeric translation would imply precision the scheduler does not provide.

## Decision

Portable contracts express workload intent and optional topology constraints. Providers report requested, effective, denied, degraded, and invalidated state. No priority or affinity success guarantees start time, completion deadline, CPU share, or isolation.

## Consequences

- Realtime claims require separate end-to-end evidence.
- Libraries cannot silently change global scheduling policy.
- Profiles can require observable placement quality without inventing numeric equivalence.

