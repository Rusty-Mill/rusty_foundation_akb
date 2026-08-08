# Attention and interruption policy

Attention intent is a semantic vector rather than a universal numeric priority: timeliness, user-actionability, ongoing-versus-transient state, sensitivity, expected frequency, expiry, and whether interruption is requested. Effective presentation remains controlled by the user and platform.

**RM-NOTIFY-ATTENTION-0001:** A producer MAY request an attention class but MUST NOT claim banner, foregrounding, sound, vibration, wake, bypass, full-screen, or immediate presentation unless a separately authorized platform capability proves it.

**RM-NOTIFY-ATTENTION-0002:** Focus/do-not-disturb, quiet hours, notification permissions/settings, per-app/category controls, screen sharing/lock state, power, session, accessibility, and rate policies MUST be respected and MUST NOT be bypassed through fallback channels.

**RM-NOTIFY-ATTENTION-0003:** Notification sounds MUST have a simultaneous non-auditory semantic path; visual presentation MUST not depend on color/image alone; motion/flashing and repeated alerts obey accessibility and safety preferences.

**RM-NOTIFY-ATTENTION-0004:** Rate limiting, coalescing, digesting, deduplication, and escalation are explicit product policy with bounded queues and stable semantic grouping. They MUST NOT discard required domain work.

**RM-NOTIFY-ATTENTION-0005:** Alarm, incoming-call, critical/emergency, communication, and system-health attention classes require specialized contracts, entitlements/policy, abuse controls, and evidence; ordinary notifications cannot emulate them.

When the application is foreground and contextually presenting the same event, product policy may suppress or adapt the system notification without losing the underlying domain state.
