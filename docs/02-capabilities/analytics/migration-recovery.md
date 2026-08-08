# Migration, recovery, and reproducibility

**RM-ANALYTICS-MIGRATE-0001:** Schema/function/plan/state/serializer/engine/connector changes classify compatibility for running jobs, checkpoints/savepoints, replay, backfill, sinks, materializations, and rollback.

**RM-ANALYTICS-MIGRATE-0002:** Stateful upgrades use versioned immutable job definitions, validated savepoint/checkpoint migration, stable operator/state identities, canary/shadow execution, output comparison, promotion, rollback, and old-state retirement.

**RM-ANALYTICS-RECOVERY-0001:** Recovery binds job/configuration/topology generation, checkpoint manifest and integrity, source replay positions/retention, state serializers, sink transaction/idempotency state, credentials, catalogs, and provider compatibility.

**RM-ANALYTICS-RECOVERY-0002:** Rescaling/repartitioning transfers complete keyed/operator/timer state with ownership fencing, duplicate/loss checks, input-frontier alignment, resource limits, and rollback.

**RM-ANALYTICS-RECOVERY-0003:** Disaster recovery tests source retention/gaps, checkpoint/savepoint/object-store/database restoration, catalog/configuration/key recovery, sink reconciliation, regional failover/failback, and materialization rebuild.

**RM-ANALYTICS-REPRO-0001:** Reproducible results bind immutable input snapshots and order, schemas/functions/code/dependencies, logical semantics, time zone/locale, numeric/float/parallel reduction policy, seeds, provider/optimizer/realized plan, resources, and nondeterminism.

**RM-ANALYTICS-REPRO-0002:** Bitwise, deterministic-order, numerically equivalent with tolerance, logically equivalent multiset, and statistically equivalent are distinct reproducibility claims with comparison methods.

**RM-ANALYTICS-MIGRATE-0003:** Provider migration uses golden semantic corpora and workload/result/plan/resource comparisons; query syntax acceptance alone does not prove equivalence.
