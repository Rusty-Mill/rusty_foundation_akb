# Schemas and semantic envelopes

**RM-MESSAGING-SCHEMA-0001:** A schema identity binds namespace, stable type/operation name, semantic revision, schema language and revision, exact content digest, compatibility policy, canonical source, generator/runtime versions, and lifecycle status. A media type or Rust type name alone is insufficient.

**RM-MESSAGING-SCHEMA-0002:** Compatibility is evaluated directionally for old/new producers and consumers and separately for wire parsing, information preservation, validation, semantics, defaults/presence, enum/union openness, unknown fields, numeric ranges, time/locale units, and security policy.

**RM-MESSAGING-SCHEMA-0003:** Field/tag/number reuse, type narrowing, changed units/defaults/presence, reordered positional fields, enum exhaustion, union changes, canonicalization changes, and required-field additions are governed by encoding-specific evolution rules and conformance fixtures.

**RM-MESSAGING-SCHEMA-0004:** Unknown fields/variants can be preserved, ignored, surfaced, quarantined, or rejected only as declared by the schema profile. Parse success does not permit executing an unknown operation or applying semantically incomplete data.

**RM-MESSAGING-SCHEMA-0005:** Envelope metadata contains only the selected profile's typed operation/event identity, schema/content encoding, logical/attempt identity, causation/correlation, source/subject, creation and expiry evidence, tenant/audience, tracing context, idempotency/deduplication token, reply/error routing, and declared extensions. Every field has authority and privacy semantics.

**RM-MESSAGING-SCHEMA-0006:** Payload and envelope are bounded independently by bytes, nesting, elements, fields, strings, allocation, recursion, decode time, expansion, attachments, and unknown data. Validation occurs before privileged dispatch and again for domain invariants.

**RM-MESSAGING-SCHEMA-0007:** Canonical encoding is required only for digest/signature/deduplication profiles and binds exact canonicalization version and semantic view. Ordinary serializer determinism is not assumed; a digest of bytes does not automatically identify semantic equivalence.

**RM-MESSAGING-SCHEMA-0008:** Schema registries/catalogs are versioned untrusted evidence sources with authenticated snapshots, namespace authority, compatibility decisions, retention, rollback/freeze protection, cache freshness, offline policy, and exact digest verification.

