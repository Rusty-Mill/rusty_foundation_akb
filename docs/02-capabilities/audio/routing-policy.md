# Audio routing and policy

Routing selects endpoints; it does not define PCM transfer. Policy inputs may include explicit endpoint selection, system default role, communications/media intent, user preference, privacy state, and product fallback.

**RM-AUDIO-ROUTE-0001:** Route selection MUST distinguish explicit endpoint binding from following a system default role.

**RM-AUDIO-ROUTE-0002:** A route change MUST publish old/new endpoint generations, reason when known, effective format/latency changes, and whether the existing stream was preserved, invalidated, or explicitly migrated.

**RM-AUDIO-ROUTE-0003:** Automatic migration MUST be opt-in policy. It creates a new stream generation and reports any gap, conversion, or clock discontinuity.

**RM-AUDIO-ROUTE-0004:** Capture, loopback capture, route override, exclusive access, global volume/mute, and background monitoring require separately attenuated authority and platform consent where applicable.

**RM-AUDIO-ROUTE-0005:** Denial, user cancellation, policy restriction, device busy, interruption, and transient unavailability MUST remain distinguishable where the platform supplies that evidence.

Product-facing route controls must have keyboard and assistive-technology equivalents, expose current effective route without relying on color or sound alone, and honor applicable mono-audio, balance, hearing-device, reduced-loud-sound, and alert preferences. Those preferences are observations; applying them to domain audio remains product/service policy.
