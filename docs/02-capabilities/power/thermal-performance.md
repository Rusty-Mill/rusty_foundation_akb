# Thermal and performance pressure

Thermal state is a qualitative, provider-defined pressure observation. It may reflect device skin temperature, component limits, policy, fan/noise targets, or predicted throttling and is not a portable temperature scale.

**RM-POWER-THERMAL-0001:** Thermal observations MUST preserve nominal/fair/serious/critical/unknown or provider-supported qualitative states with revision, source, age, and transition evidence; numeric mapping across platforms is prohibited.

**RM-POWER-THERMAL-0002:** CPU/GPU/media-engine throttling, memory pressure, energy saver, low battery, and thermal pressure MUST remain separate signals even when one causes another.

**RM-POWER-THERMAL-0003:** Workloads MUST define safe degradation and checkpoint/stop policy for pressure transitions. Critical state MAY require prompt reduction but MUST NOT be treated as a cleanup callback guarantee.

**RM-POWER-THERMAL-0004:** Providers MUST NOT promise sustained performance, clock frequency, core count, frame rate, or deadline from a thermal category or workload hint.

**RM-POWER-THERMAL-0005:** Temperature sensors, fan control, hardware health, overclocking, voltage, and power-limit manipulation are separate privileged device-management capabilities.

Performance evidence binds thermal history, power source/saver, ambient/test conditions, hardware, cooling, workload duration, and throttling observations. Short cold runs cannot substantiate sustained native-performance claims.
