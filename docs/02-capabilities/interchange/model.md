# Model, entities, and milestones

**RM-INTERCHANGE-MODEL-0001:** An interchange contract binds logical model/schema generation, format and mapping profile, canonicalization profile where selected, framing/media type/version, validation policy, compatibility, registry, limits, authority, and implementation generation.

**RM-INTERCHANGE-MODEL-0002:** Distinct entities include logical value, schema/type/field identity, ordinary encoding, canonical signed view, content bytes, frame/envelope, parser event/tree/borrowed view/owned object, unknown data, validation result, and transcoding report.

**RM-INTERCHANGE-MODEL-0003:** Milestones distinguish bytes accepted, frame complete, syntax well formed, structural limits satisfied, schema resolved, logical value constructed, semantic validation, canonical view verified, and domain authorization/effect.

**RM-INTERCHANGE-MODEL-0004:** Outcomes preserve byte/field/path/offset where safe, schema/format/profile generation, consumed/remaining bytes, partial events, unknowns, coercions/loss, canonicality, retry safety, and cleanup.

**RM-INTERCHANGE-MODEL-0005:** Encoding and decoding never imply provenance, integrity, confidentiality, authenticity, semantic safety, business validity, or authority; those compose separately.

**RM-INTERCHANGE-MODEL-0006:** Async streaming is bounded and cancellation-safe; sync equivalents never create hidden runtimes and disclose blocking, allocation, callback, and input-consumption behavior.
