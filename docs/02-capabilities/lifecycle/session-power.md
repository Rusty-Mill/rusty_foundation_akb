# Session and power observations

## Capability identities

`rm.lifecycle.session-observer` and `rm.lifecycle.power-observer` expose versioned observations of the hosting environment.

**RM-LIFECYCLE-SESSION-0001:** Session state distinguishes active/inactive, lock observation, remote/local/unknown presentation, disconnect/reconnect, and logout/termination request where available. These are observations, not authenticated user identity.

**RM-LIFECYCLE-SESSION-0002:** Application active/inactive, window focus, session active/inactive, and display visibility are independent states and cannot be derived from one another.

**RM-LIFECYCLE-POWER-0001:** Power events distinguish suspend preparation, suspended inference, resume, display-power change, thermal/power-mode observation, and shutdown/restart request where available.

**RM-LIFECYCLE-POWER-0002:** No contract guarantees delivery before suspend, hibernate, logout, shutdown, forced termination, crash, power loss, or resource-pressure kill.

**RM-LIFECYCLE-POWER-0003:** Resume creates a new observation revision and reports elapsed-clock-domain discontinuity, stale-resource categories, and required reconciliation hooks; it does not imply network, display, credential, device, or time-zone continuity.

**RM-LIFECYCLE-POWER-0004:** Observers coalesce only when final state and skipped revision range are disclosed. Loss/overflow forces a full state re-observation before continuity claims resume.

**RM-LIFECYCLE-POWER-0005:** Handlers are deadline bounded and cannot block native dispatch indefinitely. Long work is moved to ordinary async execution only if the platform keeps execution available.

