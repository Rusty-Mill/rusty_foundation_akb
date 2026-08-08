# Decode contracts and resource limits

`rm.image.decode` turns one selected item/frame into immutable pixels under an explicit plan and budget.

**RM-IMAGE-DECODE-0001:** A request MUST bind byte-source identity/generation, inspected container/item, output pixel constraints, color/orientation/alpha policy, requested scale/region/level, metadata projection, cancellation/deadline, isolation class, and resource budget.

**RM-IMAGE-DECODE-0002:** The budget MUST independently constrain input bytes, dimensions, total pixels, frames/items, components/planes, bit depth, decoded bytes, working memory, metadata/profile bytes, nesting/references, operations, CPU/wall time, output revisions, and concurrent/in-flight work.

**RM-IMAGE-DECODE-0003:** Providers use checked arithmetic before allocation and continue enforcing budgets during entropy decode, decompression, reconstruction, color transform, and output. Compression ratio, repeated frames, crafted tables, and sparse/tiled declarations MUST NOT bypass limits.

**RM-IMAGE-DECODE-0004:** Terminal outcomes distinguish unsupported feature/profile, invalid structure, truncation, integrity failure, budget/timeout/cancellation, dependency/external-reference denial, provider crash, and output conversion failure. Partial output is returned only through an explicitly selected provisional contract.

**RM-IMAGE-DECODE-0005:** Cancellation is a request; provider and output resources remain owned until terminal completion. Native callbacks cannot run arbitrary UI, plugin, I/O, or exporter code.

**RM-IMAGE-DECODE-0006:** Hardware decode is an implementation path with reported device/driver/provider, supported subset, intermediate copies/conversions, synchronization, isolation, and fallback. Hardware success neither validates the file nor strengthens fidelity.

**RM-IMAGE-DECODE-0007:** Decoder instances and mutable state are not assumed thread-safe, reusable, or reentrant. Provider resolution states concurrency, affinity, pooling, reset, and crash-containment evidence.

See [ADR-0069](../../adr/0069-decoded-images-are-bounded-immutable-resources.md).
