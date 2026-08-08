# ADR-0080: Key handles authorize operations, not key material

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Software libraries, OS key stores, secure enclaves, smart cards, TPMs, HSMs, remote services, and synchronized stores expose keys with radically different readability, operation, interaction, migration, backup, lifecycle, and assurance properties. A byte-oriented key API forces export and erases the most important security boundary.

## Decision

Symmetric and private keys are opaque, generation-scoped operation capabilities by default. A handle binds key algorithm/parameters, origin, provider/storage/protection boundary, principal/application/purpose, allowed operations, export policy, interaction, lifetime/use limits, rotation lineage, and authority. Create, use by operation, export, attest, rotate, revoke, and destroy remain independently attenuated. No provider fallback may turn a non-exportable or hardware-bound key into software bytes silently.

## Consequences

- Software byte keys remain possible only under an explicit exportable-memory policy.
- Protocols consume operations or derived handles rather than assuming key bytes.
- Backup, sync, migration, escrow, wrapping, and recovery are separate services.
- Destruction and hardware claims remain multidimensional evidence, not booleans.
