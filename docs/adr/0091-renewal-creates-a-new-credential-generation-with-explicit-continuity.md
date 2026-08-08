# ADR-0091: Renewal creates a new credential generation with explicit continuity

**Status:** Accepted  
**Date:** 2026-08-08

## Context

“Renew” may mean issue with the same key, rekey, modify identifiers, replace a lost credential, extend validity, or merely reinstall. Assuming old-key possession is always available or sufficient prevents algorithm/provider migration, mishandles compromise, and permits unauthorized claim changes.

## Decision

Every successful renewal creates a new certificate generation. Operation kind explicitly selects same-key renewal, rekey, modification, or replacement. Continuity is authenticated by a policy-selected combination of existing credential/key, account, device/workload identity, reauthorization, or approval and binds old/new keys, claims, transaction, and channel. Activation and old-credential retirement are separate milestones; executable/service rollback never implies returning to old credential or data state.

## Consequences

- Key reuse is a deliberate policy choice, not renewal semantics.
- Lost or compromised keys use recovery and revocation paths without false POP claims.
- Fleets can rotate algorithms/providers and follow issuer renewal windows safely.
- Results distinguish issued, installed, active, healthy, and retired generations.

