# Loss-prevention channels and enforcement

**RM-PROTECTION-DLP-0001:** Channel intents distinguish clipboard, drag/drop, file copy/move, removable storage, print, screen/window capture, application activation/open-in, email/message, upload/download, browser/web form, network share, cloud synchronization, API/export, logging/telemetry, AI/model prompt/output, and process/device paths.

**RM-PROTECTION-DLP-0002:** Evaluation binds exact subject/label/content evidence, principal and delegated actor, source/destination application/service/device/tenant/location, recipient/audience, action/purpose, channel generation, network/session state, policy, time, and available enforcement point.

**RM-PROTECTION-DLP-0003:** Outcomes distinguish allow, audit, notify, educate, warn, require justification, require approval, apply/raise label, protect, redact/transform, route to managed destination, quarantine, block, defer/unknown, and unsupported enforcement.

**RM-PROTECTION-DLP-0004:** A policy decision is not a channel effect. Enforcement revalidates subject/destination/recipient generations at the native effect boundary and returns attempted, prevented, transformed, transferred, partially transferred, recipient-accepted, and indeterminate separately.

**RM-PROTECTION-DLP-0005:** Multi-item/batch operations define all-or-none, per-item, prefix, or best-effort semantics; policy tips aggregate safely without hiding which items differ, and cancellation reports every item/channel effect.

**RM-PROTECTION-DLP-0006:** Unsupported, stale, offline, encrypted/opaque, provider-unavailable, unmanageable, or bypassable channels follow explicit fail-closed/fail-open/restrict/review policy by risk and never silently claim prevention.

**RM-PROTECTION-DLP-0007:** DLP cannot claim universal exfiltration prevention. Reports name covered channels, applications, identities, devices, data forms, timing windows, alternate encodings, and known bypass/residual paths.

**RM-PROTECTION-DLP-0008:** Channel hooks cannot disclose content to policy, cloud, audit, or UI beyond separately authorized projections and minimize sensitive matching evidence.
