# Leases and fencing

**RM-COORDINATION-LEASE-0001:** A lease binds coordination domain/configuration, resource/scope, holder principal and instance generation, lease generation/ID, granted TTL, monotonic acquisition/renewal evidence, quorum/provider, permissions, fencing token, and expiration uncertainty.

**RM-COORDINATION-LEASE-0002:** Requested TTL, granted TTL, locally estimated remaining time, server expiry, quorum-recognized expiry, revocation, and resource-enforced fencing are distinct. Wall-clock display is diagnostic only unless a selected bounded-clock protocol proves more.

**RM-COORDINATION-LEASE-0003:** Renewal is a new quorum/provider-confirmed state transition with deadline and attempt identity. A queued/sent/locally successful keepalive, recent heartbeat, or cached TTL never extends authority by itself.

**RM-COORDINATION-FENCE-0001:** Every successful exclusive lease/leadership/lock generation carries a monotonically ordered, non-reused fencing token scoped to the protected resource and authority domain. Token comparison semantics and overflow/recovery are explicit.

**RM-COORDINATION-FENCE-0002:** Each protected stateful side-effect boundary atomically rejects tokens older than the greatest accepted token before mutation. Cooperative checks only in clients or the coordination service cannot prevent a paused or partitioned stale holder from acting.

**RM-COORDINATION-FENCE-0003:** Multi-resource work declares how fencing composes across resources and transactions. If any target cannot enforce fencing, exclusivity is best-effort evidence and destructive/non-idempotent operations require another safety mechanism.

**RM-COORDINATION-LEASE-0004:** Release/revoke is idempotent and reports provider acceptance separately from holder stop, work drain, resource fencing, and effect completion. Lease loss cancels authority immediately but cleanup remains bounded reconciliation.

**RM-COORDINATION-LEASE-0005:** Suspend/hibernation, VM pause/snapshot, GC/runtime stall, clock step/slew, network partition, server failover, credential rotation, and process fork/clone invalidate local lease-confidence assumptions and are mandatory tests.

