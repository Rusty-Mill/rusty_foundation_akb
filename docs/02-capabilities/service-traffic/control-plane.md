# Control-plane lifecycle and propagation

**RM-TRAFFIC-CONTROL-0001:** Control-plane resources are immutable versioned service/cluster/endpoint/route/listener/security/policy graphs with referential integrity, authority, dependencies, compatibility, and activation order.

**RM-TRAFFIC-CONTROL-0002:** Clients acknowledge received, validated, accepted, rejected, locally applied, warmed, serving, draining, and retired generations separately with error/resource evidence.

**RM-TRAFFIC-CONTROL-0003:** Incremental and state-of-world updates preserve coherent snapshots, deletion/tombstones, nonce/revision, dependency ordering, duplicate/gap/reconnect reconciliation, and bounded backlog.

**RM-TRAFFIC-CONTROL-0004:** Last-known-good policy has maximum age, security-revocation exceptions, dependency retention, restart persistence, downgrade prevention, and explicit behavior when no valid generation exists.

**RM-TRAFFIC-CONTROL-0005:** Progressive configuration rollout defines target fleet/subset, compatibility, preflight/warmup, staged percentage, health guardrails, pause/rollback, mixed-generation limits, completion evidence, and cleanup.

**RM-TRAFFIC-CONTROL-0006:** Rollback selects a newly authorized coherent generation and accounts for endpoint/application/data evolution; it is not an assumption that old configuration remains safe.

**RM-TRAFFIC-CONTROL-0007:** Administrative writes use least privilege, optimistic concurrency, idempotency, approval/quorum for high impact, immutable audit, emergency freeze/revoke, and recovery.

**RM-TRAFFIC-CONTROL-0008:** Propagation objectives measure distribution, validation/application, new traffic behavior, and observed request outcomes separately across clients, proxies, regions, and protocols.
