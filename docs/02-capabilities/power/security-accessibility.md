# Power security, privacy, and accessibility

Observation is read-only and minimally scoped. Assertions, system power transitions, wake scheduling, charging/device policy, and performance controls carry progressively stronger authority and abuse potential.

**RM-POWER-SECURITY-0001:** Leases and power requests MUST be attributable, auditable, scoped, revocable, and bounded; untrusted plugins/remote inputs cannot acquire them without attenuated authority and host policy.

**RM-POWER-SECURITY-0002:** User idle detection, presence, lid state, battery history, assertion reason, sleep/wake timing, and power-source changes MUST be privacy classified and MUST NOT be repurposed as identity, surveillance, or behavioral profiling data.

**RM-POWER-SECURITY-0003:** Applications MUST NOT prevent user-requested sleep/shutdown indefinitely, suppress critical-power action, spoof system battery/thermal warnings, or silently change system-wide power/charging settings.

**RM-POWER-ACCESS-0001:** Power/thermal adaptation MUST preserve accessible operation and provide nonvisual, localized state when reduced quality, deferred work, cancellation, or data-risk action affects the user.

**RM-POWER-ACCESS-0002:** User-visible lease reasons and blockers MUST be concise and accessible; any cancel/release/control UI supports keyboard and assistive technology.

**RM-POWER-ACCESS-0003:** Reduced motion, contrast, text scaling, captions, audio alternatives, and assistive-device connectivity MUST not be disabled to meet energy goals without explicit user-controlled policy.
