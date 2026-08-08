# Logical data, records, keys, and queries

**RM-PERSISTENCE-DATA-0001:** Logical types specify nullability/presence, signedness/range/precision/scale, exact text/bytes/UUID, date/time/time-zone/calendar semantics, enum/union openness, arrays/maps/records, collation, normalization, and application invariants independently of provider storage types.

**RM-PERSISTENCE-DATA-0002:** Conversion plans declare source/target logical and provider types, loss/rounding/truncation/overflow, encoding, time zone, collation, invalid-value policy, canonicalization, and round-trip evidence. Silent coercion is prohibited for material data.

**RM-PERSISTENCE-DATA-0003:** Keys bind type/schema, equality/order/hash/collation semantics, generation, tenant namespace, mutability, allocation/uniqueness mechanism, and reuse/tombstone policy. Display labels, row positions, timestamps, or provider physical identifiers are not durable application identity by default.

**RM-PERSISTENCE-QUERY-0001:** A query intent is a typed relational/key/document operation graph with inputs, projection, predicates, joins/lookups, grouping/aggregation, ordering, limits/page semantics, snapshot/consistency, result schema, resource budget, and authority—not raw provider text.

**RM-PERSISTENCE-QUERY-0002:** Provider-native query text/AST remains an explicit extension with exact dialect/version, parameter binding, result schema, read/write classification, statement limits, security review, and portability status. String interpolation is prohibited.

**RM-PERSISTENCE-QUERY-0003:** Parameters are typed values bound separately from syntax with count/size/lifetime/sensitivity limits. Provider plans cannot reinterpret untrusted identifiers, directions, clauses, or object names as value parameters.

**RM-PERSISTENCE-QUERY-0004:** Result sets/streams expose exact column/field identity and type, null/presence, row version/snapshot, ordering guarantee, truncation/warnings, partial progress, cursor generation, and completion. Iteration does not imply buffering or transaction survival.

**RM-PERSISTENCE-QUERY-0005:** Pagination declares stable order, snapshot/consistency, keyset/cursor/offset semantics, opaque cursor scope/freshness/integrity, inserts/deletes behavior, page-size limits, and end/gap/duplicate outcomes. Offset alone does not promise stable pages.

**RM-PERSISTENCE-QUERY-0006:** Query planning/analysis is evidence with provider/version, schema/statistics generation, estimated cost/cardinality, index/partition choices, cache, parameters, warnings, and actual-plan distinction; it grants no execution authority.

