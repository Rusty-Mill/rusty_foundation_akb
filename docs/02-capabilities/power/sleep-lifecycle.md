# Sleep, wake, and lifecycle integration

Power observation complements [application lifecycle session/power events](../lifecycle/session-power.md). Lifecycle owns suspend/resume milestones; this domain owns power/energy context and assertions. Neither guarantees callback delivery before sleep or shutdown.

**RM-POWER-SLEEP-0001:** Awake, preparing-to-sleep, suspended/unknown, resuming, and reconciled MUST be distinct lifecycle observations with generation and clock-discontinuity evidence.

**RM-POWER-SLEEP-0002:** Applications MUST continuously maintain durable correctness and checkpoint interruptible work; pre-sleep callbacks and delay assertions are optional bounded opportunities.

**RM-POWER-SLEEP-0003:** Resume MUST revalidate clocks, timers, network, devices, mounts, capture/audio streams, leases, credentials, and external assumptions before resuming work.

**RM-POWER-SLEEP-0004:** Requested system sleep/hibernate/restart/power-off and scheduled wake are separate privileged services with authentication, multi-session policy, inhibition handling, platform availability, and explicit user interaction.

**RM-POWER-SLEEP-0005:** Wake timers/alarms MUST state whether they wake hardware, merely become eligible after wake, require AC, survive reboot, and are subject to policy/coalescing. Ordinary deadline timers imply none of these.

**RM-POWER-SLEEP-0006:** Modern standby/background execution, maintenance windows, wake-on-network, and platform task schedulers require specialized profiles and energy/security evidence.
