# Security, privacy, and accessibility

**RM-REMOTE-INTERACTION-QUALITY-0001:** Session establishment MUST mutually bind authenticated peer/channel evidence, current grants, local login/security-context generation, and an anti-replay transcript before view or control becomes active.

**RM-REMOTE-INTERACTION-QUALITY-0002:** Remote input payloads, captured content, participant identity, titles/topology, clipboard/files, audit records, and usage metadata are sensitive and MUST follow minimization, encryption, retention, disclosure, and telemetry-redaction policy.

**RM-REMOTE-INTERACTION-QUALITY-0003:** Control policy MUST rate-limit and audit denied as well as accepted security-relevant transitions without logging entered text, secrets, raw pixels, or precise interaction traces by default.

**RM-REMOTE-INTERACTION-QUALITY-0004:** Consent, participant/role state, view/control indication, handoff, warnings, errors, and emergency stop MUST be keyboard and screen-reader operable, magnification/high-contrast compatible, localized, bidirectional-text safe, and not dependent on color or motion alone.

**RM-REMOTE-INTERACTION-QUALITY-0005:** Remote assistance MUST coexist with local assistive technology. Injected input MUST NOT disable accessibility, seize exclusive focus, or suppress local accessibility actions; conflicts and semantic degradation are explicit.

**RM-REMOTE-INTERACTION-QUALITY-0006:** Products MUST disclose when keyboard-only, text entry, touch, pen, gestures, audio description, captions, or assistive-technology behavior cannot be faithfully conveyed or controlled.

**RM-REMOTE-INTERACTION-QUALITY-0007:** Accessibility authority and APIs MUST NOT be repurposed as an invisible general injection bypass. Accessibility-originated semantic commands remain separately authorized and attributed.
