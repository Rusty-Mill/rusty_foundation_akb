# Snapshots, changes, and atomic application

**RM-APP-SYNC-CHANGE-0001:** A snapshot names dataset/schema/policy generation, selection, causal/sequence frontier, included objects and tombstones, consistency scope, creation method, integrity, and omissions.

**RM-APP-SYNC-CHANGE-0002:** A change set is an immutable ordered or partially ordered group with stable identity, dependencies, preconditions, operations, effect semantics, atomicity boundary, and content digests.

**RM-APP-SYNC-CHANGE-0003:** Full-state, operation, delta, event, and patch transfer are distinct representations. JSON Patch, merge patch, binary deltas, and provider change feeds do not independently define domain merge semantics.

**RM-APP-SYNC-CHANGE-0004:** Inbound data is bounded, authenticated, decoded, schema-resolved, semantically validated, authorized, and conflict-evaluated before becoming visible.

**RM-APP-SYNC-CHANGE-0005:** Applying a change set is atomic across its declared boundary or records independently retryable item outcomes. Checkpoint advancement follows durable application, not mere receipt or parse.

**RM-APP-SYNC-CHANGE-0006:** Duplicate, reordered, overlapping, missing, corrupt, truncated, and dependency-incomplete changes produce deterministic rejection, buffering, repair, or resnapshot behavior with bounded resources.
