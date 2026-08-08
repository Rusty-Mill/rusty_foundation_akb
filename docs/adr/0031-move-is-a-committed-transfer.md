# ADR-0031: Move is a committed transfer, not a pointer gesture

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

A cross-application move can fail during rendering, streaming, import, target persistence, acknowledgement, or source deletion. Native APIs distinguish preferred and performed effects imperfectly, and cross-filesystem moves are often copy-plus-delete. Deleting source data on drop acceptance risks loss; never deleting makes move misleading.

## Decision

Move is a multi-stage protocol. The target freezes an accepted operation/representation, materializes and validates content, commits target state, then returns an explicit committed result. Only then may the source apply its declared deletion/mutation policy. Source cleanup failure is a distinct completed-with-source-remnant outcome, never rolled into target failure silently.

## Consequences

- Pointer release and hover feedback never authorize deletion.
- Cross-application move is generally not globally atomic.
- Item-level and transaction-level semantics must be declared.
- Recovery can identify duplicates, remnants, and partial target artifacts honestly.

