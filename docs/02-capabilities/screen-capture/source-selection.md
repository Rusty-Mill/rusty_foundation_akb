# Source selection and identity

## Model

A `CaptureSourceDescriptor` is non-authoritative evidence with `kind` (`display`, `window`, `application_group`, `region`, or `virtual_display`), opaque provider identity, generation, user-facing label/thumbnail policy, owner evidence, geometry revision, availability, and supported selection qualities. A `CaptureSourceGrant` is an opaque authority created or confirmed by a trusted selector and bound to source generation, application identity, purpose, allowed output classes, selection time, interaction/session context, and revocation channel.

**RM-SCREEN-CAPTURE-SOURCE-0001:** Source enumeration and trusted source selection MUST be separate operations; neither enumeration, a native handle, a title, a process identity, nor coordinates authorize capture.

**RM-SCREEN-CAPTURE-SOURCE-0002:** The default selection path MUST use platform-controlled UI where available and MUST preserve cancel, denial, restriction, unavailable, and unknown as distinct outcomes.

**RM-SCREEN-CAPTURE-SOURCE-0003:** A grant MUST identify the selected source kind and generation, requesting application, purpose, permitted cursor/audio/output qualities, native authority provenance, and revocation mechanism without exposing a forgeable native token.

**RM-SCREEN-CAPTURE-SOURCE-0004:** A source becoming unavailable, reused, replaced, or ambiguously remapped MUST NOT silently transfer authority to another source; continued capture requires provider-proven continuity or explicit reselection.

**RM-SCREEN-CAPTURE-SOURCE-0005:** Region selection MUST bind its coordinate space, owning source generation, transform revision, and clipping rule. It MUST NOT become a floating desktop rectangle after topology or scale changes.

**RM-SCREEN-CAPTURE-SOURCE-0006:** Labels, thumbnails, application ownership, minimized state, and geometry are privacy-sensitive observations and MUST follow explicit minimization, freshness, redaction, and retention policy.

## Selection modes

Applications may constrain which kinds are acceptable, whether multiple sources are permitted, and which of their own surfaces are excluded from picker results. They cannot preselect unrelated content, obscure the selected boundary, or reinterpret a user-selected window as its containing display. Restorable selection hints are untrusted, single-purpose inputs and require current provider validation and any native reconfirmation.
