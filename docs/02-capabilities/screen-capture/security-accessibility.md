# Security, privacy, and accessibility

**RM-SCREEN-CAPTURE-QUALITY-0001:** Capture MUST default to trusted, foreground, user-visible source selection and MUST preserve native privacy indicators, stop controls, and revocation paths.

**RM-SCREEN-CAPTURE-QUALITY-0002:** Applications MUST present an accessible persistent statement of what source and auxiliary streams are active, why, who receives them, and how to stop or change them.

**RM-SCREEN-CAPTURE-QUALITY-0003:** Picker invocation, source selection, consent, preview, active indication, errors, and stop/change controls MUST support keyboard, screen reader, magnification, high contrast, reduced motion, and localized/bidirectional text.

**RM-SCREEN-CAPTURE-QUALITY-0004:** Nonvisual selection MUST not depend solely on thumbnails, color, screen position, transient borders, or drag gestures; source labels and relationships require meaningful accessible alternatives.

**RM-SCREEN-CAPTURE-QUALITY-0005:** Frames, thumbnails, titles, owner identities, cursor traces, audio, source history, and topology are sensitive. Logs and telemetry MUST default to metadata-only redacted summaries with explicit retention and disclosure authority.

**RM-SCREEN-CAPTURE-QUALITY-0006:** Secure fields, notifications, accessibility overlays, magnifiers, remote-session surfaces, virtual displays, and recording indicators MUST have tested inclusion/exclusion semantics and explicit nonclaims.

**RM-SCREEN-CAPTURE-QUALITY-0007:** Capture authority MUST NOT imply permission to persist, upload, recognize, index, train on, retransmit, or expose output to plugins or other principals.

Products must supply content-specific consent, recipient disclosure, retention, moderation, and legal policy. Rusty Mill supplies the mechanism boundaries and evidence, not those product decisions.
