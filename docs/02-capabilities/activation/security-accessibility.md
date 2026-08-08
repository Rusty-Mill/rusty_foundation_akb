# Security, privacy, and accessibility

**RM-ACTIVATION-SECURITY-0001:** Handler discovery, default observation, chooser, file/URI/app activation, writable handoff, registration, default settings, install recommendation, and acknowledgment use separate authority and user-interaction policy.

**RM-ACTIVATION-SECURITY-0002:** Activation MUST NOT implicitly invoke a shell, executable search, interpreter, script engine, installer, elevated helper, network fetch, or direct process spawn. Those require separate explicit contracts and policy.

**RM-ACTIVATION-SECURITY-0003:** Background/plugin/remote requests are rate-limited and cannot create prompt storms, steal foreground, expose chooser/history/defaults, or transfer sensitive capabilities without explicit product/user policy.

**RM-ACTIVATION-PRIVACY-0001:** Targets, filenames/paths, URIs/payloads, handler/default lists, application identities, recent-use evidence, activation history, source/referrer, session, and domain results are sensitive and omitted or minimized in telemetry.

**RM-ACTIVATION-ACCESS-0001:** Handler chooser, confirmation, default-settings guidance, progress, denial, ambiguity, and recovery are keyboard/switch/screen-reader operable, localized/bidirectional, zoom/high-contrast compatible, and preserve focus without surprise.

**RM-ACTIVATION-ACCESS-0002:** Choices expose semantic app identity, supported role, target type, access requested, trust/source, default/one-time effect, and consequences without relying only on icons, color, order, popularity, or truncatable filenames.

**RM-ACTIVATION-ACCESS-0003:** Incoming activation routes to an accessible state and announces material result once; duplicate deliveries, startup queues, focus denial, or delayed readiness MUST NOT create repeated announcements or inaccessible orphan windows.
