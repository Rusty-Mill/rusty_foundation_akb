# Transcoding and loss accounting

**RM-INTERCHANGE-TRANSCODE-0001:** A transcode plan binds source bytes/format/profile/schema, decoded logical model, target schema/format/profile, resolution/coercion policy, unknown/extension handling, canonical/signature effects, limits, and authority.

**RM-INTERCHANGE-TRANSCODE-0002:** Reports classify lost/changed presence, defaults, numeric range/precision/lexical form, NaN/negative zero, binary/text/Unicode, time zone/precision, key types/duplicates/order, enum/union, references/cycles, unknowns/extensions, metadata, and canonical identity.

**RM-INTERCHANGE-TRANSCODE-0003:** Lossless claims require source-to-target-to-source logical and required representation invariants over the declared value domain; successful parse and write are insufficient.

**RM-INTERCHANGE-TRANSCODE-0004:** Signed, MACed, encrypted, compressed, or content-addressed bytes are not transcoded in place; verification/decryption, logical transformation, new canonical view, and new protection are separate authorized operations with provenance.

**RM-INTERCHANGE-TRANSCODE-0005:** Unknown fields and extensions are preserved only when the target can represent their exact required semantics/bytes and policy permits it; opaque wrapping is distinct from native mapping.

**RM-INTERCHANGE-TRANSCODE-0006:** Streaming transcoding declares whether container lengths/order/canonicalization require buffering, sorting, spill, multiple passes, or reject unbounded inputs.

**RM-INTERCHANGE-TRANSCODE-0007:** Best-effort coercion is opt-in, never used for security/policy/signature values, and returns per-path diagnostics plus an unambiguous degraded status.
