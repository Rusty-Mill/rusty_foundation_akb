# Types, schemas, and columnar batches

**RM-ANALYTICS-TYPE-0001:** Logical types preserve null/missing distinctions, signedness/width, decimal precision/scale/rounding/overflow, float NaN/infinity/signed-zero, strings/binary, date/time/timestamp/time zone, duration/interval, list/map/struct/union, dictionary, extension, and application semantics.

**RM-ANALYTICS-TYPE-0002:** Schemas bind stable field identity, name, type, nullability, ordering, metadata, defaults, constraints, semantic units, classification, evolution generation, and nested lineage rather than relying on names alone.

**RM-ANALYTICS-TYPE-0003:** Record batches contain equal-length typed arrays with explicit validity, offsets, lengths, child/dictionary references, alignment, ownership, mutability, lifetime, and buffer-size validation.

**RM-ANALYTICS-TYPE-0004:** Zero-copy is a qualified representation/lifetime property, not a semantic guarantee; crossing trust, device, process, encoding, alignment, endianness, compression, encryption, or ownership boundaries may require validated copying.

**RM-ANALYTICS-TYPE-0005:** Row, columnar, file, wire, database, vectorized, CPU/GPU, and provider-native conversions report coercion, truncation, precision, time-zone, collation, null, nested, dictionary, extension, and metadata loss.

**RM-ANALYTICS-TYPE-0006:** Batch construction and slicing prevent offset/length overflow, buffer alias mutation, invalid UTF/extension data, child-length mismatch, oversized allocation, decompression bombs, and unbounded nesting.

**RM-ANALYTICS-TYPE-0007:** Schema evolution classifies compatible projection, widening, nullable/default addition, rename/identity preservation, reinterpretation, narrowing, and reprocessing-required changes with mixed-generation rules.
