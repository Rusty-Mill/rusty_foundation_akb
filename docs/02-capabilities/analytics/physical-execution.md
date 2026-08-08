# Physical planning and distributed execution

**RM-ANALYTICS-PHYSICAL-0001:** A physical plan binds logical plan generation, provider and optimizer versions/configuration, statistics snapshot, partitioning/order properties, operator algorithms, exchange topology, parallelism, memory/spill/device policy, adaptive rules, and authority.

**RM-ANALYTICS-PHYSICAL-0002:** Planning reports chosen and rejected alternatives where diagnostic policy permits, estimates versus observed values, unsupported semantics, pushdowns, approximations, adaptive decision points, and reproducibility limitations.

**RM-ANALYTICS-PHYSICAL-0003:** Partitioning declares hash/range/round-robin/single/source semantics, key encoding/collation/null behavior, partition count/generation, ordering, skew, and rescaling compatibility.

**RM-ANALYTICS-PHYSICAL-0004:** Exchanges/shuffles bind attempt and partition generations, producer/consumer sets, materialization/durability, compression/encryption/checksums, flow control, retry/deduplication, locality, cleanup, and data classification.

**RM-ANALYTICS-PHYSICAL-0005:** Task attempts use immutable input splits and output identities; speculative/retried attempts commit conditionally so only one authorized generation becomes visible.

**RM-ANALYTICS-PHYSICAL-0006:** Adaptive execution may change algorithms, partitioning, joins, skew handling, or parallelism only at declared barriers while preserving logical semantics and recording the realized plan.

**RM-ANALYTICS-PHYSICAL-0007:** Partial stage/task success is not query success. Coordinators reconcile orphaned shuffle/state/output artifacts and ambiguous task/sink acknowledgments.
