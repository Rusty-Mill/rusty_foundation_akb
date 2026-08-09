# Brokers, agents, and provider protocols

**RM-SECRETS-BROKER-0001:** A broker publishes provider identity/version, protection and availability claims, supported secret/credential classes, operations, interaction, export forms, lease semantics, limits, consistency, replication, recovery, and audit behavior.

**RM-SECRETS-BROKER-0002:** Broker agents run under a separately restricted identity, expose a least-authority local endpoint, authenticate and isolate callers, prevent cross-tenant/confused-deputy access, bound caches, and cannot be bypassed through ambient provider credentials.

**RM-SECRETS-BROKER-0003:** Remote protocol plans bind exact service identity, endpoint, secure channel, client/workload authentication, namespace/mount/path, request schema, redirects/proxies, retry/idempotency, rate limits, deadlines, and disclosure.

**RM-SECRETS-BROKER-0004:** Provider tokens used by a broker are audience- and namespace-limited, preferably renewable/dynamic, never forwarded to dependents, rotated independently, and excluded from diagnostics and crash artifacts.

**RM-SECRETS-BROKER-0005:** Broker caching binds secret/lease generation, caller/audience, expiry, revocation frontier, offline policy, memory domain, and eviction/zeroization claim. Persistent caching requires a separately selected protected-store contract.

**RM-SECRETS-BROKER-0006:** Failover and replication preserve coherent versions, lease ownership, revocation queues, monotonic security epochs, target reconciliation, and split-brain controls; availability never authorizes stale secret issuance by itself.
