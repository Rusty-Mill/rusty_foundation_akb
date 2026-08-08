# Notification conformance specification

| Area | Required evidence |
|---|---|
| Content | localization/plurals/bidi, truncation, action labels, images/sounds/markup, size/action limits, unsupported degradation |
| Submission | accepted/rejected categories, registration/package/session failures, rate limits, exactly scoped success claims |
| Attention | per-app/category denial, focus/quiet hours, lock/shared screen, foreground state, sound/motion/accessibility preferences |
| Milestones | accepted/presented/suppressed/unknown, response/dismiss/expire/withdraw, callback loss, history support/nonclaims |
| Actions | default/buttons/input, cold/running/redirection activation, duplicate/late/replay, stale revision, auth/confirmation and idempotency |
| State | atomic/best-effort replacement, progress sequencing/rate, badge bounds, withdrawal after response, external dismissal |
| Scheduling | civil gaps/overlaps/timezone/clock changes, sleep/reboot/logout/update/removal, missed/duplicate triggers, reconciliation |
| Privacy | lock-screen redaction, shared/remote session, sensitive content/actions/input, image origins, telemetry/history/provider sync |
| Accessibility | screen reader, keyboard/switch access, sound-off/visual alternatives, high contrast, text scaling, concise update announcements |

Conformance runs against representative native notification centers and desktop environments, not only mocked adapters. Reports bind OS/build/desktop/compositor, application packaging/identity, provider version, notification settings/focus/session/lock state, locale/accessibility settings, supported-capability discovery, and every delivery/retention/activation nonclaim.

Fault injection covers service restart/unavailability, registration loss, queue/rate saturation, malformed content, stale updates, process death, simultaneous action and withdrawal, duplicated activation, clock change, reboot, and user settings changes.
