# `rm.profile.foundation.desktop`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 1.0.0 |
| Purpose | Interactive user-session foundation with durable files and user-protected secrets |

## Workload assumptions

A logged-in graphical user session may permit consent/authentication prompts, but UI responsiveness and accessibility semantics are mandatory future gates. Windowing, input, accessibility, and i18n capabilities are explicit gaps, so this is not a complete desktop profile.

## Required capabilities

**RM-PROFILE-FOUNDATION-DESKTOP-0001:** Requires the [CLI foundation](foundation-cli.md) capability set plus `rm.filesystem.atomic-replace` `>=0.1.0,<0.2.0` and `rm.security.secret-store` `>=0.1.0,<0.2.0`.

Additional constraints:

- **RM-PROFILE-FOUNDATION-DESKTOP-0002:** Filesystem resolution is at least R1; application-owned sensitive state requires the strongest provider level available under policy and records it.
- **RM-PROFILE-FOUNDATION-DESKTOP-0003:** Atomic replacement declares visibility and durability separately; critical state requests D2 or reports unsatisfied.
- **RM-PROFILE-FOUNDATION-DESKTOP-0004:** Secret storage is user/application bound, reboot-persistent, and available in the declared logged-in/unlocked state.
- **RM-PROFILE-FOUNDATION-DESKTOP-0005:** Prompting may occur only through an async path coordinated with the application UI; sync UI-thread prompting is prohibited.
- **RM-PROFILE-FOUNDATION-DESKTOP-0006:** Secret synchronization and backup behavior are explicit profile inputs, never inherited from provider defaults silently.

## Optional services

Orderly shutdown may coordinate document/state flush. Restricted execution and authority attenuation may isolate plugins or content processing, but no plugin system is implied until its domain contract exists.

## Evidence gates

Tests cover locked/unlocked session transitions, prompt cancellation, logout/login, app sandbox/container context, backup/sync policy, filesystem durability context, suspend/resume timing, and UI-thread nonblocking behavior. Accessibility of native prompts remains a provider evidence obligation when prompting is enabled.

## History

- **1.0.0:** Incorporates CLI foundation 1.0.0 process launch/control and optional pipe/resolution contracts.
- **0.1.0:** Initial interactive runtime, filesystem, and secret-store trial.
