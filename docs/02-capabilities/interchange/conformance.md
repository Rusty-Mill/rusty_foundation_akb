# Conformance vectors

**RM-INTERCHANGE-CONFORMANCE-0001:** Logical/schema vectors cover every type, boundary number, presence/default/null/missing, duplicate/order, Unicode/normalization, time/zone, recursive/nested, enum/union/extension, constraints, and invalid value.

**RM-INTERCHANGE-CONFORMANCE-0002:** Format vectors include normative valid encodings, alternate valid forms, canonical/deterministic forms, malformed/truncated/trailing data, overlong lengths/numbers, duplicates, unknowns, invalid Unicode/tags/wire types, and implementation differentials.

**RM-INTERCHANGE-CONFORMANCE-0003:** Evolution matrices execute old/new writer-reader pairs across stored/replayed/forwarded values, unknown preservation, field/tag reservation, presence/default, enum/union, maps, text projections, rollback, and semantic assertions.

**RM-INTERCHANGE-CONFORMANCE-0004:** Canonical suites require exact bytes and digest/signature-domain vectors across implementations/languages/platforms, reject out-of-domain/noncanonical ambiguity, and test unknowns, floats, Unicode, maps/sets, defaults, and schema/profile substitution.

**RM-INTERCHANGE-CONFORMANCE-0005:** Streaming/framing suites split every byte boundary, concatenate messages, truncate/falsify lengths, cancel/resume, apply backpressure, test compression expansion, negotiation downgrade, trailing bytes, and recovery/quarantine.

**RM-INTERCHANGE-CONFORMANCE-0006:** Hostile suites fuzz grammar/structure/schema, depth/cardinality/length/integer overflow, hash collisions/duplicate keys, regex/validation complexity, references, lazy indexes, constructors/extensions, error amplification, and memory lifetime.

**RM-INTERCHANGE-CONFORMANCE-0007:** Transcoding matrices compare logical and required representation invariants, loss reports, unknown/extension handling, signed/canonical invalidation, streaming buffer bounds, and best-effort rejection zones.

**RM-INTERCHANGE-CONFORMANCE-0008:** Registry/lifecycle suites test conflicting allocation, equivocation/rollback, dependency cycles, compatibility races, alias promotion, revocation/offline cache, generated-artifact provenance, backup/restore/failover, and access controls.

**RM-INTERCHANGE-CONFORMANCE-0009:** Provider reports publish unsupported semantics, deviations/extensions, weaker guarantees, configuration, versions, limits, conversion loss, performance, and waivers.
