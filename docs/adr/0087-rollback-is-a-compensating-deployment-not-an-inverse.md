# ADR-0087: Rollback is a compensating deployment, not an inverse

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Installers run hooks, modify registrations and services, merge configuration, migrate data, rotate credentials, and cross native points of no return. Native package managers may expose half-installed or partially configured states. Reversing an operation log cannot reliably restore prior external state and may corrupt newer data.

## Decision

Rollback is a newly resolved and authorized deployment from authoritative current state to an eligible target generation. It validates retained artifacts and current trust/revocation, compatibility of configuration/data/checkpoints/services, downgrade policy, and health gates; journals compensating work; and reports residual or ambiguous state. Executable rollback never implies data rollback.

## Consequences

- Last-known-good is evidence, not merely a version label.
- Recovery may complete forward, compensate, repair, quarantine, or require an operator.
- Hooks and migrations require idempotency/reconciliation and explicit compatibility.
- Products must retain suitable artifacts and recovery capacity to promise rollback.

