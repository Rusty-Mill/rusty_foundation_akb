# Wire encodings and format mappings

**RM-INTERCHANGE-WIRE-0001:** Each mapping binds exact standard/version/profile, media type/parameters, schema representation, type/field/variant mapping, presence/default, numeric/text/binary/time, ordering/duplicates, unknowns, extensions, canonicality, and limits.

**RM-INTERCHANGE-JSON-0001:** JSON profiles define object-member duplicates/order, number domain and lexical form, Unicode/escape/surrogate handling, top-level values, null/missing, binary/time/decimal mapping, extensions, and I-JSON/canonical restrictions where selected.

**RM-INTERCHANGE-CBOR-0001:** CBOR profiles define tags, integer/bignum/decimal/float, definite/indefinite lengths, map-key types/duplicates/order, embedded data, shared references, unknown tags, deterministic rules, and application semantics.

**RM-INTERCHANGE-MSGPACK-0001:** MessagePack-style profiles define spec/version, extension type registry, integer/float/string/binary selection, maps/duplicates/order, timestamp mapping, unknown extensions, and deterministic profile if required.

**RM-INTERCHANGE-PROTO-0001:** Field-tagged schema mappings define wire types, tag reservation, presence, packed repeated fields, maps, enums, oneof/unions, unknown fields, groups/extensions, JSON/text projections, and deterministic noncanonical limitations.

**RM-INTERCHANGE-ASN1-0001:** ASN.1 profiles bind abstract syntax modules/object identifiers, constraints, open types, tagging, BER/CER/DER/PER/OER/XER/JER rule selection, defaults/sets/order, extension markers, and canonical/security requirements.

**RM-INTERCHANGE-WIRE-0002:** Format auto-detection is bounded evidence and never silently chooses security- or schema-critical semantics; protocols use explicit media type, framing, magic/version, or negotiated profile.

**RM-INTERCHANGE-WIRE-0003:** Implementation extensions and nonconforming legacy modes are separately identified, disabled by default at untrusted boundaries, and covered by compatibility and security evidence.
