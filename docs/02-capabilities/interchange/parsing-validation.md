# Parsing, validation, and hostile input

**RM-INTERCHANGE-PARSE-0001:** Parsers default to strict well-formedness and declare accepted extensions, duplicate/trailing/unknown behavior, recovery mode, and differences between diagnostic and production parsing.

**RM-INTERCHANGE-PARSE-0002:** Limits cover total bytes, frames/items, nesting/depth, fields/map keys, array elements, string/binary/token length, number digits/exponents, references, dictionaries/tags/extensions, allocations, CPU, recursion, diagnostics, and time.

**RM-INTERCHANGE-PARSE-0003:** Length/offset/count arithmetic is checked before allocation or pointer/slice formation; malformed input cannot cause overflow, out-of-bounds, use-after-free, stack exhaustion, or disproportionate work.

**RM-INTERCHANGE-PARSE-0004:** Syntax, structural/schema, constraint, semantic/business, canonical, provenance/integrity, and authorization validation are separately typed stages.

**RM-INTERCHANGE-PARSE-0005:** Validation errors identify stable rule and bounded redacted path/offset plus actual/expected class without echoing secrets or attacker-sized content.

**RM-INTERCHANGE-PARSE-0006:** Fail-fast and collecting validation define maximum errors/work, ordering, dependent-rule suppression, partial-object exposure, and accessibility/localization of diagnostics.

**RM-INTERCHANGE-PARSE-0007:** Recovery/salvage tools never label damaged or skipped input as normally decoded and cannot feed security/domain processing without explicit quarantine and revalidation.

**RM-INTERCHANGE-PARSE-0008:** Deserialization never invokes arbitrary constructors, code, filesystem/network access, dynamic type loading, or object-graph callbacks without separately granted capability and isolation.
