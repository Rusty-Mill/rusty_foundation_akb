# Resource, action, and scope semantics

**RM-APP-AUTHZ-RESOURCE-0001:** Resource types publish stable type identity, immutable instance generation, tenant/namespace, parent/containment and ownership semantics, supported actions, attribute schema, relation schema, lifecycle, and enforcement boundary.

**RM-APP-AUTHZ-RESOURCE-0002:** Actions are semantic domain operations such as read metadata, read content, update, delete, share, delegate, approve, publish, administer, or assume—not transport verbs or UI labels unless the product contract makes them identical.

**RM-APP-AUTHZ-RESOURCE-0003:** Scope is typed and canonical: exact resource, descendants under declared hierarchy semantics, collection/query, field/projection, data region, operation parameters, purpose, time, network/device, or effect limit. String-prefix containment is prohibited unless explicitly specified.

**RM-APP-AUTHZ-RESOURCE-0004:** Resource aliases, moves, copies, links, forks, snapshots, restores, imports, and tenant transfers define whether identity, ownership, grants, denies, relations, labels, and history are preserved, re-evaluated, or rejected.

**RM-APP-AUTHZ-RESOURCE-0005:** Creation authorization distinguishes permission to create within a parent from authority over the not-yet-existing child and defines initial owner, attributes, relations, grants, labels, and rollback semantics atomically.

**RM-APP-AUTHZ-RESOURCE-0006:** Composite operations enumerate sub-effects and either enforce atomically, stage under a validated plan, or report partial outcomes; a coarse parent permit cannot authorize undeclared sub-effects.
