# Logical data model and schema identity

**RM-INTERCHANGE-SCHEMA-0001:** Logical types distinguish null/missing, boolean, signed/unsigned integers and ranges, decimal, binary floating values, text/binary, date/time/zone/duration, enum, sequence, set, map, record, tagged union, reference, opaque, and extension semantics.

**RM-INTERCHANGE-SCHEMA-0002:** A schema has immutable namespace/name/version or content identity, stable type/field/variant identifiers, type/cardinality/presence/default, constraints, semantic units, documentation, deprecation, privacy classification, and authority.

**RM-INTERCHANGE-SCHEMA-0003:** Field names, numeric tags, OIDs, map keys, array positions, and host-language member names are separate identifiers connected by a versioned format mapping.

**RM-INTERCHANGE-SCHEMA-0004:** Presence distinguishes absent, explicit null, default-valued, empty, unknown, and redacted states where the logical contract requires them; formats unable to preserve a distinction report loss or reject it.

**RM-INTERCHANGE-SCHEMA-0005:** Numeric semantics define domain, precision/scale, rounding, overflow, negative zero, NaN/infinity/payload, and integer/float interchange; text defines Unicode scalar/byte validity and normalization policy.

**RM-INTERCHANGE-SCHEMA-0006:** Map/set equality, duplicate keys/elements, ordering, key types, union discrimination, enum openness, reference/cycle identity, and recursive depth are explicit.

**RM-INTERCHANGE-SCHEMA-0007:** Host-language generated/reflected types are projections of the logical schema and disclose representation, ownership, unknown-field, validation, and evolution limitations.
