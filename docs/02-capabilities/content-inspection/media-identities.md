# Media identities, registries, and declarations

**RM-CONTENT-MEDIA-0001:** Media identity includes namespace/registry, canonical type and parameters, specification/profile/version, structured suffix where applicable, aliases/deprecations, and registry snapshot generation; a bare extension or unqualified string is insufficient.

**RM-CONTENT-MEDIA-0002:** HTTP/content declarations, archive/package metadata, filesystem associations, filename extensions, Uniform Type Identifiers, application registrations, user overrides, and detector outputs preserve source and precedence independently.

**RM-CONTENT-MEDIA-0003:** Media parameters such as charset, codecs, boundary, profile, version, and compression are parsed under the exact specification. Unknown, duplicate, invalid, or contradictory parameters are not normalized into false agreement.

**RM-CONTENT-MEDIA-0004:** Registry aliases and inheritance express compatibility hints, not parser substitution or security equivalence. Product policy selects accepted canonical identities and profiles.

**RM-CONTENT-MEDIA-0005:** Association lookup is purpose- and platform-scoped and may return multiple ranked applications/types. User defaults do not prove content structure, and detection does not select an application or authorize activation.

**RM-CONTENT-MEDIA-0006:** Extensionless, multi-extension, hidden-extension, bidirectional/control-character, case, Unicode, trailing-space/dot, alternate-stream, and compound-name cases retain raw and display-safe evidence.
