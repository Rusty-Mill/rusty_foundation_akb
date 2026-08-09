# Conflict detection and merge policy

**RM-APP-SYNC-CONFLICT-0001:** Conflict detection is defined per object/field/relation/invariant and distinguishes concurrent intent, failed precondition, uniqueness/integrity collision, delete-update, move/rename, authorization change, and schema incompatibility.

**RM-APP-SYNC-CONFLICT-0002:** Merge policy is versioned and typed: reject/rebase, authoritative-side wins, deterministic register, set/map/list CRDT, operational transformation, three-way semantic merge, custom resolver, or human resolution.

**RM-APP-SYNC-CONFLICT-0003:** A resolver receives immutable base/ancestor where available, concurrent inputs, causal and actor evidence, schema/policy generations, authority, and limits; it emits a new resolution change with provenance rather than rewriting history.

**RM-APP-SYNC-CONFLICT-0004:** Last-writer-wins declares the compared clock/order, tie-breaker, delete semantics, skew/fault assumptions, and accepted data loss. It is not the default for safety-, money-, identity-, authorization-, or rights-relevant state.

**RM-APP-SYNC-CONFLICT-0005:** CRDT use specifies state/op/delta form, algebra, delivery assumptions, duplicate/reorder behavior, causal context, invariant limitations, metadata growth, garbage collection, and schema evolution.

**RM-APP-SYNC-CONFLICT-0006:** OT use specifies operation space, transform/inclusion properties, central-order or peer assumptions, undo/redo, cursor/presence mapping, history retention, and convergence evidence.

**RM-APP-SYNC-CONFLICT-0007:** Unresolved conflicts remain first-class, queryable, access-controlled state. A deterministic display winner cannot discard or hide losing intent without policy.
