# Budgets, power, network, and concurrency

**RM-BACKGROUND-BUDGET-0001:** Every workload declares CPU time/share/QoS, wall duration, memory, I/O, network, storage, wakeup, concurrency, and energy/thermal expectations plus minimum useful work and degradation policy.

**RM-BACKGROUND-BUDGET-0002:** Native budgets, quotas, priorities, idle/maintenance opportunity, power/network requirements, and deadlines are policy requests and observations, not guaranteed resources or continued-execution promises.

**RM-BACKGROUND-BUDGET-0003:** The runtime MUST expose warning/cancellation/expiration callbacks under restricted execution rules and require incremental checkpointing; callbacks are not guaranteed before abrupt termination.

**RM-BACKGROUND-BUDGET-0004:** Work MUST tolerate loss of network, credentials, mounts, devices, session, and service dependencies. Eligibility is rechecked at irreversible side effects, not only at attempt start.

**RM-BACKGROUND-BUDGET-0005:** Concurrency is bounded per definition, principal, host, dependency, and resource class. Fairness and starvation policy MUST be explicit across tenants and foreground workloads.

**RM-BACKGROUND-BUDGET-0006:** Background policy MUST NOT weaken integrity, durability, security, accessibility, or required user notification merely to fit a budget; the work defers or fails explicitly.

**RM-BACKGROUND-BUDGET-0007:** Sync control surfaces use finite deadlines over the same asynchronous broker state and MUST NOT create a hidden runtime, nested UI loop, or indefinite service-manager wait.
