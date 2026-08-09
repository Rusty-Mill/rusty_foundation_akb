# ADR-0143: Communication preference is scoped evidence

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

A global subscribed/unsubscribed boolean cannot represent multiple tenants, purposes, topics, channels, endpoints, sender programs, mandatory service notices, quiet hours, consent sources, or endpoint reassignment. Treating transactional as a bypass label also invites abuse.

## Decision

Consent, subscription, opt-out, channel preference, frequency, quiet hours, suppression, and mandatory exceptions remain typed, scoped, provenance-bearing assertions. Eligibility is a versioned policy derivation performed before attempts and revalidated where required. Exceptions are narrow, accountable, and auditable.

## Options considered

- One global boolean: easy to operate but over- and under-suppresses.
- Provider lists as authority: delegates policy and fragments channels.
- Scoped evidence plus derivation: more state, but explicit and reconcilable; selected.

## Consequences

Preference centers and unsubscribe handlers need clear scopes. Suppression must propagate across providers/caches. Products and qualified legal/privacy owners define classifications and exceptions; Rusty Mill provides mechanisms and evidence, not legal conclusions.
