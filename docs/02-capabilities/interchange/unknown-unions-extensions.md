# Unknown fields, unions, and extensions

**RM-INTERCHANGE-UNKNOWN-0001:** Unknown fields preserve exact tag/key identity, wire type/representation or normalized value as specified, occurrence/order where semantically needed, size limits, provenance, and forwarding policy.

**RM-INTERCHANGE-UNKNOWN-0002:** Unknown preservation is not comprehension or authority. Intermediaries may forward only under schema/profile/security policy and cannot inspect/rewrite/sign unknown semantics as understood data.

**RM-INTERCHANGE-UNKNOWN-0003:** Unknown data may be lost through text/JSON projection, field-by-field copy, transcoding, canonicalization, generated types, merge, map conversion, or storage; every such boundary declares loss.

**RM-INTERCHANGE-UNION-0001:** Tagged unions bind discriminator identity and payload schema; unknown variants remain distinguishable from absent/not-set and preserve enough representation for permitted forwarding.

**RM-INTERCHANGE-UNION-0002:** Untagged unions require deterministic non-overlapping resolution or explicit ambiguity policy and are prohibited where multiple variants accept the same hostile input without a stable choice.

**RM-INTERCHANGE-EXT-0001:** Extension namespaces allocate stable identifiers through governed registries, collision/reservation rules, ownership, status, schema/profile constraints, criticality, and lifecycle.

**RM-INTERCHANGE-EXT-0002:** Critical unknown extensions cause rejection; noncritical extensions can be ignored/preserved only as the protocol defines, with no silent change in signed or business semantics.

**RM-INTERCHANGE-UNKNOWN-0004:** Merge semantics for repeated singular fields, maps with duplicate keys, messages/records, unions, and unknowns are explicit and conformance-tested.
