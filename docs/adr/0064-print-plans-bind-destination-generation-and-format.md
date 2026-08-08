# ADR-0064: Print plans bind destination generation and document format

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Printer options form a constraint system, not independent flags. Native capability results can depend on queue/device configuration, ready media, driver/service generation, policy, credentials, and document format. Reusing a ticket after a destination or representation change can silently substitute or invalidate user intent.

## Decision

A resolved print plan binds one destination/capability generation, document identity and exact representation format, complete requested intent, effective values, substitutions/degradations, and validation evidence. Required constraints fail rather than default silently. The whole plan is revalidated immediately before native submission; stale generations trigger renegotiation, not automatic retargeting.

## Consequences

- Capability queries carry document format and revision context.
- Print panels return structured intent/evidence rather than opaque authorization to print anything later.
- Caches key the complete destination, format, policy, and provider generation.
