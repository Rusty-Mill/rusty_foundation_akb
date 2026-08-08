# ADR-0039: Restoration state is disposable continuity metadata

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native restoration systems may discard archives, reject versions, omit forced-quit state, or rebuild only portions of a UI. Using restoration archives as the authoritative store risks data loss and stale authority replay.

## Decision

Restoration state is versioned, integrity-checked, disposable continuity metadata above durable domain persistence. It carries identifiers and approved ephemeral UI/editing state, never durable-record ownership, secrets, native handles, or authority. Restore revalidates every reference under current policy.

## Options considered

- Treat restoration as persistence: convenient but unsafe and platform-dependent.
- Disable restoration: robust but degrades continuity.
- Layer restoration over durable state: preserves UX without weakening correctness.

## Consequences

- Restoration can fail partially and fall back safely.
- Products need explicit archive schemas, migration, expiry, and privacy review.
- Durable data services cannot defer commits until termination.

