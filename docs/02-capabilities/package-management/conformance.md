# Package-management conformance

Every report binds provider/native manager and version, OS/architecture/scope/root, installed and repository generations, plan/policy/trust digests, fixtures, authority mode, network/time/power environment, and result evidence.

**RM-PACKAGE-CONFORMANCE-0001:** Repository tests cover valid role/delegation rotation plus expired, rollback, freeze, mix-and-match, fast-forward, wrong-target, mirror equivocation, corrupt/truncated/oversized metadata/artifacts, offline bundles, delta reconstruction, cache poisoning, and bounded failover.

**RM-PACKAGE-CONFORMANCE-0002:** Resolver tests cover native version edge cases, dependency ranges/predependencies/alternatives/virtual providers, cycles, conflicts/replacements, architecture/co-install, channels/pins/holds, downgrades/removals, multiple solutions, unsatisfiable graphs, deterministic explanation, and stale inputs.

**RM-PACKAGE-CONFORMANCE-0003:** Plan/authority tests mutate every artifact, target, source, scope, privilege, hook, choice, policy, installed generation, volume, restart/reboot, and expiry input and prove revalidation or rejection.

**RM-PACKAGE-CONFORMANCE-0004:** Transaction fault injection covers every phase and point of no return under cancel, crash, kill, reboot, power loss, disk/inode/quota exhaustion, read-only/corrupt/removed volume, database lock/corruption, concurrent native manager, permission loss, and journal damage.

**RM-PACKAGE-CONFORMANCE-0005:** Filesystem/archive tests cover traversal, absolute/reserved paths, symlink/hardlink/reparse/mount races, case/Unicode/normalization collisions, duplicate/overlap, metadata/ACL/capability/label preservation, device/special files, decompression bombs, and cross-volume behavior.

**RM-PACKAGE-CONFORMANCE-0006:** Hook/service/data tests cover old/new scripts, triggers, undeclared effects, idempotency, timeout/crash/output bounds, dependency absence, service drain/coexist/restart/readiness, configuration merge/conflict, migration/checkpoint compatibility, secret handling, and residual ownership.

**RM-PACKAGE-CONFORMANCE-0007:** Rollout tests cover deterministic cohorts, pause/abort/promotion thresholds, missing/late/biased health evidence, offline devices, mandatory deferral/deadline, active work, bandwidth/concurrency, emergency revocation, rollback eligibility, and privacy/accessibility.

**RM-PACKAGE-CONFORMANCE-0008:** Recovery tests start from every supported partial/native state and prove resume, forward-complete, compensate, repair, quarantine, removal, or operator-required results without invented atomicity or data rollback.

**RM-PACKAGE-CONFORMANCE-0009:** Cross-platform suites include MSIX and declared classic Windows variance, Debian/dpkg and RPM-family transactions, macOS bundles/packages, managed and direct channels, user/machine/offline roots, and native evidence mapping.

