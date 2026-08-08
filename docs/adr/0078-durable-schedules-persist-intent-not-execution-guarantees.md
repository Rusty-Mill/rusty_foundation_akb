# ADR-0078: Durable schedules persist intent, not execution guarantees

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native schedulers interpret wall-clock recurrence, monotonic intervals, idle/maintenance opportunities, boot/login events, power/network requirements, quotas, and missed work differently. Devices sleep, clocks and time zones change, policies disable tasks, and applications update while work is pending. A registered schedule cannot guarantee exact launch or execution.

## Decision

A durable schedule is immutable, generation-bound intent containing its temporal domain and rule, time-zone/database and ambiguity policy where civil, earliest/deadline window, flexibility, eligibility constraints, missed-run and overlap policy, workload/package generation, authority, and expiration. Registration acceptance proves only that the provider accepted that intent. Attempts and application results have separate durable evidence.

## Consequences

- Exact wall-clock execution and exactly-once execution are not base claims.
- Sleep, downtime, clock/rule changes, quota, and policy produce explicit missed/coalesced/deferred outcomes.
- Domain exactly-once effects require idempotency, durable work claims, and reconciliation.
- Updates explicitly migrate, replace, retain, or expire pending schedule generations.
