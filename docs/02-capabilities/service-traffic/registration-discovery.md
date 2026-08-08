# Registration, leases, and discovery

**RM-TRAFFIC-REGISTER-0001:** Registration binds authenticated workload/service identity, endpoint generation, address/protocol/capability, locality, metadata, readiness policy, lease/expiry, configuration generation, and ownership authority.

**RM-TRAFFIC-REGISTER-0002:** Lease renewal proves only current registrar acceptance for the lease scope; process life, reachability, readiness, authorization, or successful requests remain separate.

**RM-TRAFFIC-REGISTER-0003:** Deregistration, expiry, drain, crash, partition, replacement, and administrative disable are distinct lifecycle events with idempotent reconciliation and stale-registration cleanup.

**RM-TRAFFIC-DISCOVERY-0001:** Discovery returns an expiring revisioned snapshot or reconciled change stream of candidate endpoints plus source/provenance, TTL/lease, completeness/partial state, ordering/priority/weight hints, and security validation.

**RM-TRAFFIC-DISCOVERY-0002:** DNS A/AAAA/SRV/SVCB/HTTPS, OS-native discovery, static configuration, registries, orchestrator endpoint sets, and xDS-like control planes retain their own cache, alias, negative, consistency, watch, and authentication semantics.

**RM-TRAFFIC-DISCOVERY-0003:** Watches/notifications trigger snapshot reconciliation; they are not assumed lossless, ordered, duplicate-free, or complete journals unless the provider contract proves it.

**RM-TRAFFIC-DISCOVERY-0004:** Clients bound alias depth/loops, record/endpoints/metadata, watch backlog, update rate, stale retention, negative caching, parsing, and network work.

**RM-TRAFFIC-DISCOVERY-0005:** Network, namespace, tenant, proxy, and resolver context partitions discovery caches; network changes and authority/policy changes invalidate or revalidate observations.

**RM-TRAFFIC-DISCOVERY-0006:** When discovery is unavailable or stale, fail-closed, last-known-good, direct fallback, alternate source, and offline behavior are explicit with maximum age and security downgrade policy.
