# Notification privacy, security, and accessibility

Notifications may be visible on locked, shared, projected, remotely viewed, recorded, or glanceable surfaces and may be retained by platform history or synchronized externally.

**RM-NOTIFY-PRIVACY-0001:** Every notification MUST carry a privacy class and locked/shared-screen presentation policy. Sensitive content defaults to a generic redacted summary with no secret-bearing image, action, input, or sound.

**RM-NOTIFY-PRIVACY-0002:** Secrets, authentication factors, recovery codes, full message bodies, health/financial details, precise location, and private filenames MUST NOT appear unless explicit product policy and user settings authorize the exact surface.

**RM-NOTIFY-PRIVACY-0003:** Notification payloads, action input, identifiers, images, and history MUST be minimized in telemetry/crash data and protected according to retention and provider-sync exposure.

**RM-NOTIFY-SECURITY-0001:** URLs, protocol activations, images, markup, remote content, action input, and provider callbacks are untrusted. Rendering and activation MUST use typed allowlisted schemas and ordinary authority checks.

**RM-NOTIFY-ACCESS-0001:** Content MUST be understandable when images, sound, color, motion, or truncation are unavailable and MUST use logical reading order, concise labels, localized text, and meaningful action names.

**RM-NOTIFY-ACCESS-0002:** Notification actions and settings MUST be keyboard and assistive-technology operable; time-limited actions allow sufficient time or an equivalent application path.

**RM-NOTIFY-ACCESS-0003:** Products MUST avoid excessive announcements and interruption; batching and updates preserve semantic changes without causing repeated full live-region output.
