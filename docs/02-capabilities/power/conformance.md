# Power and energy-management conformance specification

| Area | Required evidence |
|---|---|
| Sources/batteries | AC/battery/UPS, multi-battery/dock/hot-swap, charge states, unknowns, estimate volatility, units/overflow, source restart |
| Policy | saver/low-power transitions, locked/unavailable state, foreground/background, adaptation hysteresis and minimum quality |
| Thermal | qualitative transitions, unavailable sensors, sustained throttling, interaction with saver/battery and safe degradation |
| Leases | each target, grant/degrade/deny/override/expiry, renewal, owner crash, plugin/session retirement, critical battery/lid/user sleep |
| Lifecycle | missed/delayed pre-sleep, suspend/resume clock and resource reconciliation, shutdown, modern standby/background restrictions |
| Budgets | measurement boundary/calibration/uncertainty, observation lag, unavailable attribution, enforcement/recovery |
| Security/privacy | least authority, remote/plugin denial, assertion leakage, no critical-action suppression, telemetry/history minimization |
| Accessibility | accessible blocker/reason/adaptation UX, reduced-quality alternatives, assistive features preserved under energy policy |

Test matrices cover desktops without batteries, laptops/tablets, multiple batteries/docks, UPS, VM/remote/container sessions, saver modes, low/critical charge, charging/discharging/unknown rate, sleep/hibernate where available, lid close, power-source change, thermal load, service restart, and abrupt power/suspend simulation. Reports bind OS/build, hardware/firmware/battery, provider, power profile/saver, source, thermal/cooling/ambient conditions, session/privilege, lease target, workload, and all estimate/request nonclaims.
