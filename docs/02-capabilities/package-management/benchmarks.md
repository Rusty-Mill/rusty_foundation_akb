# Package-management benchmarks

**RM-PACKAGE-BENCH-0001:** Measure metadata refresh/verification, inventory observation, resolution, plan generation/approval, fetch, delta reconstruction, artifact verification, staging, commit, hook/service work, activation, health, reconciliation, rollback, repair, removal, and cleanup separately and end to end.

**RM-PACKAGE-BENCH-0002:** Workloads cover one package, typical application plus runtime, large application, many small files, deep/wide dependency graphs, conflicts/alternatives, multiple architectures/languages, large installed inventories, full/delta updates, warm/cold caches, and offline/slow/lossy mirrors.

**RM-PACKAGE-BENCH-0003:** Report latency distributions, time to candidate/plan/staged/committed/active/healthy, metadata/artifact/network bytes, delta ratio, hash throughput, disk reads/writes/amplification, peak space, memory, allocations, CPU, lock wait, hook time, restarts/reboots, cancellation and recovery latency.

**RM-PACKAGE-BENCH-0004:** Sustained fleet tests report eligibility/offer/download/install/health coverage, concurrency/bandwidth adherence, retry/backoff, mirror load, cohort fairness, pause latency, failure amplification, and offline/unknown denominators without collecting unrestricted inventory.

**RM-PACKAGE-BENCH-0005:** Fault benchmarks quantify recovery after every phase under power/crash/disk/database/service failure, retained-space cost, successful automatic reconciliation, operator-required rate, and time to restored healthy service.

**RM-PACKAGE-BENCH-0006:** Compare native manager, Rusty Mill adapter, and full authenticated update path only with equivalent signatures, dependency semantics, hooks, durability, restart/reboot, and health guarantees. Classic arbitrary installers are a separate class.

Initial budgets remain RFC-owned after representative Windows, Linux, and macOS baselines exist.

