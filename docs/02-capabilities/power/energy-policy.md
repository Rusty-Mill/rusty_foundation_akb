# Energy saver and workload adaptation

Energy/low-power saver is a revisioned policy observation. Application adaptation consumes it with product workload requirements, user preference, foreground/background state, deadlines, thermal pressure, connectivity, and quality constraints.

**RM-POWER-POLICY-0001:** Saver state MUST distinguish enabled, disabled, automatically active, unavailable, policy-locked, and unknown where the provider supports those states.

**RM-POWER-POLICY-0002:** Workload intent MUST describe latency sensitivity, user visibility, deferrability, throughput floor, quality alternatives, background eligibility, and cancellation/checkpoint behavior rather than request an OS-specific power mode by name.

**RM-POWER-POLICY-0003:** Adaptation changes—rate, resolution, polling, concurrency, batching, animation, prefetch, background work, hardware acceleration, or quality—MUST be explicit product policy with minimum accessibility/correctness constraints.

**RM-POWER-POLICY-0004:** Effective requested/degraded/denied/overridden intent MUST be observable where supported; no hint guarantees CPU frequency, device power state, energy allocation, latency, or completion.

**RM-POWER-POLICY-0005:** Energy adaptation MUST NOT disable security validation, encryption, data integrity, accessibility, required user feedback, or durable commits.

**RM-POWER-POLICY-0006:** Policy oscillation MUST be controlled with explicit hysteresis/debounce and bounded convergence without hiding urgent critical-power changes.
