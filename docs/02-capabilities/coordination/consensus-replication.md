# Consensus and replicated state

**RM-COORDINATION-CONSENSUS-0001:** A consensus profile names algorithm/protocol revision, safety and liveness properties, crash/Byzantine/storage/network/clock failure model, membership transition, quorum/fault domains, stable storage, authentication, transport, snapshot/compaction, and implementation evidence.

**RM-COORDINATION-CONSENSUS-0002:** Term/ballot/epoch, log index, proposal, accepted/replicated, committed, applied, read index/lease, snapshot, configuration, and client result are distinct ordered evidence. A majority write is not necessarily committed without the selected algorithm's rules.

**RM-COORDINATION-CONSENSUS-0003:** Replicated state-machine commands are deterministic over exact prior state and schema/version context, with canonical validation, bounded execution, no ambient I/O/time/randomness, and explicit side-effect outputs. External effects occur after commit through fenced idempotent reconciliation.

**RM-COORDINATION-CONSENSUS-0004:** Client request deduplication binds client incarnation, sequence/request identity, operation digest, result, retention, snapshot/recovery, and authorization. Expired or restored dedup state weakens replay guarantees explicitly.

**RM-COORDINATION-CONSENSUS-0005:** Reads declare linearizable/read-index/leader-lease/sequential/snapshot/bounded-stale/local semantics, configuration and applied-index preconditions, clock assumptions, quorum/path, and freshness evidence. Serving from a leader does not alone prove a linearizable read.

**RM-COORDINATION-CONSENSUS-0006:** Snapshots bind cluster/configuration, last included term/index, state schema/digest, application/dedup/fencing state, encryption/signature, creation atomicity, transfer bounds, installation verification, and log-retention relation.

**RM-COORDINATION-CONSENSUS-0007:** Log compaction, truncation, repair, restore, force-new-cluster, quorum replacement, and unsafe bootstrap are separately privileged recovery operations with data-loss/split-brain impact, immutable plans, fencing, audit, and post-recovery identity generations.

**RM-COORDINATION-CONSENSUS-0008:** Consensus orders chosen commands; it does not validate application semantics, authorize callers, make handlers deterministic, atomically commit unrelated databases, or guarantee progress during partition or insufficient quorum.

