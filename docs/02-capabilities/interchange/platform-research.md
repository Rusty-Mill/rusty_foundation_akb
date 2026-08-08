# Platform and standards research

## Standards evidence

- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html) defines JSON syntax and interoperability constraints; [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) defines one JSON canonicalization scheme over a constrained domain.
- [RFC 8949](https://www.rfc-editor.org/rfc/rfc8949.html) defines CBOR data items, preferred serialization, tags, deterministic encoding profiles, streaming considerations, and hostile-decoder requirements.
- [Protocol Buffers language and evolution guidance](https://protobuf.dev/programming-guides/proto3/) defines field tags, presence, unknown preservation, reservations, binary-safe and conditionally compatible changes; its [encoding guidance](https://protobuf.dev/programming-guides/encoding/) explicitly distinguishes deterministic from canonical serialization.
- [ITU-T X.690](https://www.itu.int/rec/T-REC-X.690/en) defines BER, CER, and DER encoding rules for ASN.1 abstract values, including canonical/distinguished profiles.
- [MessagePack specification](https://github.com/msgpack/msgpack/blob/master/spec.md) defines a compact object representation and extension types but product protocols still choose schema, duplicate/order, deterministic, and evolution semantics.

## Platform conclusions

Windows, Linux, and macOS provide bytes, text, I/O, memory mapping, cryptography, locale/time, and IPC/network primitives through existing capabilities. None supplies a universal logical schema, evolution, canonicalization, validation, or registry contract.

**RM-INTERCHANGE-RESEARCH-0001:** Portability preserves logical semantics, schema/profile identities, compatibility/loss, canonical bytes, limits, and evidence—not identical host types, map iteration, reflection, generated APIs, allocation, or performance.

**RM-INTERCHANGE-RESEARCH-0002:** Providers disclose standard/version deviations, accepted noncanonical forms, unknown/duplicate/union behavior, numeric/text/time mappings, deterministic guarantees, limits, lazy/zero-copy lifetimes, and schema evolution.

**RM-INTERCHANGE-RESEARCH-0003:** Product RFCs select exact profiles; a generic “JSON,” “CBOR,” “protobuf,” “ASN.1,” or “MessagePack” label is insufficient for signed, persisted, or compatibility-sensitive data.
