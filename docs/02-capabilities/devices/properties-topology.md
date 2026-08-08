# Device properties and topology

Properties use namespaced stable keys with declared type, multiplicity, unit, encoding, provenance, sensitivity, volatility, availability, and snapshot revision. Unknown keys remain preservable diagnostic data but do not acquire portable meaning.

**RM-DEVICE-PROPERTY-0001:** Portable property keys MUST define value type, unit/encoding, sensitivity, volatility, absence semantics, and authoritative source class.

**RM-DEVICE-PROPERTY-0002:** Missing, unsupported, redacted, temporarily unavailable, malformed, and retrieval-failed MUST remain distinguishable.

**RM-DEVICE-PROPERTY-0003:** Native strings and byte properties MUST be length-bounded and validated at the adapter boundary; display strings are untrusted and localized only by the product layer.

**RM-DEVICE-PROPERTY-0004:** Mutable properties MUST be revision-bound and MUST NOT be cached as immutable identity evidence.

Topology is a typed multigraph. Edge kinds include `physical-parent`, `logical-parent`, `transport`, `driver-service`, `function-of`, `member-of`, and `class-endpoint`. Providers state whether each edge is native, inferred, or unavailable.

**RM-DEVICE-TOPOLOGY-0001:** Topology edges MUST identify kind, provenance, observation revision, and endpoint generations.

**RM-DEVICE-TOPOLOGY-0002:** Consumers MUST NOT infer physical containment, trust, shared failure domain, bandwidth, or power dependency from an untyped parent/child relation.

**RM-DEVICE-TOPOLOGY-0003:** Cycles, multi-parent graphs, virtual nodes, aggregate devices, and missing ancestors MUST be representable.
