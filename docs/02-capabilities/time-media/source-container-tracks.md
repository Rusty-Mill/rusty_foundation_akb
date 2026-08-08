# Media source, container, and tracks

`rm.media.source-inspector` performs bounded probe and structural inspection over explicit byte-stream authority. It composes the image probe rule: detection evidence never establishes trust.

**RM-MEDIA-SOURCE-0001:** A source descriptor MUST state identity/generation, seekability and byte-range quality, known/unknown length, live/growing/final state, latency/cache/provenance, integrity evidence, external-reference policy, and change/discontinuity behavior.

**RM-MEDIA-CONTAINER-0001:** Probe results preserve MIME/extension/signature/brand/provider evidence, ambiguity, bytes inspected, streaming/seek/index requirements, confidence, truncation, and terminal/incomplete state separately.

**RM-MEDIA-CONTAINER-0002:** An immutable presentation snapshot MUST expose container/profile/brands, duration/time origin quality, track/program/group relationships, chapters, attachments, timed metadata, index/random-access evidence, encryption/protection descriptors, and unknown/vendor structures under bounds.

**RM-MEDIA-TRACK-0001:** Each track descriptor MUST carry provider-scoped identity/generation, kind, codec/profile/level/configuration bytes under policy, time base, start/duration/edit mapping, language/role/labels, default/forced/autoselect, audio/video/text format, dependencies, encryption, and provenance/unknowns.

**RM-MEDIA-TRACK-0002:** Track, elementary stream, representation/rendition, program, angle, audio description, commentary, captions, subtitles, metadata, chapters, and attachment are typed relationships. Display order and default flags do not grant authority or prove user preference.

**RM-MEDIA-TRACK-0003:** Track enumeration and selection MUST NOT instantiate decoders, fetch external resources, acquire licenses, or execute attachments. Provider support is an operation/profile/security vector, not one `supports format` boolean.

**RM-MEDIA-CONTAINER-0003:** Offsets, sizes, counts, nesting, indexes, edit lists, sample tables, references, and durations use checked arithmetic and explicit bounds. Contradictory indexes/timestamps and cycles are rejected or quarantined with provenance.
