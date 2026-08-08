# Staging and transactions

**RM-PACKAGE-TRANSACTION-0001:** Deployment proceeds through explicit `preflight`, `fetch`, `verify`, `stage`, `prepare`, `commit`, `activate`, `reconcile`, and `cleanup` milestones; unsupported native atomicity and points of no return are declared before execution.

**RM-PACKAGE-TRANSACTION-0002:** Fetching and staging are bounded, cancellable, content-addressed where feasible, isolated from active executable paths, and safe under duplicate work. Every staged artifact receives signed-artifact acceptance under the plan policy.

**RM-PACKAGE-TRANSACTION-0003:** Preflight validates plan freshness, authority/elevation, package database lock/health, space/inodes/quotas, filesystem semantics, target volume, running-use policy, service/session state, restore/rollback capacity, power, and reboot constraints.

**RM-PACKAGE-TRANSACTION-0004:** A durable journal records plan digest, native transaction identifier, phase, completed/pending actions, points of no return, artifacts, generations, hook/service outcomes, recovery instructions, and integrity. Journal secrets and sensitive paths are minimized.

**RM-PACKAGE-TRANSACTION-0005:** File replacement preserves package ownership and required metadata, permissions, labels, ACLs, capabilities, links, extended attributes, code signatures, and atomicity/durability claims. Cross-volume or non-atomic behavior is explicit.

**RM-PACKAGE-TRANSACTION-0006:** Commit means the native package database/filesystem reached its declared boundary. Activation, readiness, restart, reboot completion, health, and user-visible success are later milestones.

**RM-PACKAGE-TRANSACTION-0007:** Cancellation is accepted only at declared safe boundaries. After a point of no return it becomes stop-after-safe-point, reconciliation, or compensating action rather than a claim that nothing changed.

**RM-PACKAGE-TRANSACTION-0008:** Concurrent deployments use native locking or explicit serialization. Deadlock, lock ownership, wait/cancel, abandoned transaction, external-manager activity, and stale-plan behavior are evidence-bearing.

**RM-PACKAGE-TRANSACTION-0009:** Power loss, crash, disk-full, device removal, process termination, reboot, native-manager restart, and corrupt journal resume through idempotent reconciliation from installed truth; caller retry does not duplicate irreversible actions.

