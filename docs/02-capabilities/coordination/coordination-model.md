# Coordination model and authority

**RM-COORDINATION-MODEL-0001:** A coordination domain binds stable cluster/service identity, protocol/provider/build, participant and configuration generations, failure model, quorum rules, consistency profile, clock assumptions, storage/durability, network topology, tenant, authority, and recovery policy.

**RM-COORDINATION-MODEL-0002:** Participant, process, instance, session, member, replica, voter, learner/witness, leader, lease holder, lock owner, transaction coordinator, and client are distinct identities with generation and role evidence. Restart never preserves an instance generation implicitly.

**RM-COORDINATION-MODEL-0003:** Every coordination operation binds exact domain/configuration generation, principal and attenuated authority, operation/resource identity, deadline/cancellation, consistency and durability requested, preconditions/version, idempotency, limits, and immutable attempt identity.

**RM-COORDINATION-MODEL-0004:** Submitted, locally persisted, sent, received, proposed, quorum-replicated, committed, applied, externally fenced, acknowledged, observed, snapshot-included, compacted, and recovered are separate milestones with boundary and proof quality.

**RM-COORDINATION-MODEL-0005:** Client libraries expose unavailable, timeout, cancellation, stale configuration/leader, rejected precondition, lost quorum, uncertain commit, applied-but-response-lost, fenced, conflict, corrupt, and unrecoverable distinctly. No timeout becomes an automatic failure or success decision.

**RM-COORDINATION-MODEL-0006:** Discovery and health data identify candidates, not cluster membership, leadership, authority, or consistency. Every privileged operation is accepted only by the selected coordination domain under its current authenticated configuration.

**RM-COORDINATION-MODEL-0007:** Async-first watches and operations are bounded, loss-aware, and cancellation-safe. Sync-complete equivalents preserve generations and evidence and never start hidden runtimes, infinite keepalives, or automatic mutation retries.

