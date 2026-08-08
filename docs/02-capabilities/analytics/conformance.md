# Conformance

**RM-ANALYTICS-CONFORMANCE-0001:** Type/batch suites use golden nested/null/decimal/float/time-zone/interval/dictionary/extension corpora, malformed offsets/lengths/buffers, conversions, schema evolution, zero-copy lifetime, and cross-provider round trips.

**RM-ANALYTICS-CONFORMANCE-0002:** Logical suites compare expressions, coercions, null/error, functions, joins, bags/sets, windows, aggregates, ordering, nondeterminism, time/calendar/DST, approximate errors, and rewrite equivalence against reference results.

**RM-ANALYTICS-CONFORMANCE-0003:** Source/format suites inject concurrent publication, corrupt/truncated/encrypted files, manifests/listings, schema/partition drift, change duplicates/gaps/tombstones, pushdown differentials, and catalog/statistics changes.

**RM-ANALYTICS-CONFORMANCE-0004:** Distributed suites inject task/coordinator/worker/network/storage failure during scan/shuffle/spill/speculation/adaptation and verify conditional output, bounded retries, no cross-attempt mixing, cleanup, and partial-result evidence.

**RM-ANALYTICS-CONFORMANCE-0005:** Streaming suites generate out-of-order/late/duplicate/gapped events, idle/new/recovered partitions, watermark skew/alignment, windows/triggers/retractions, state TTL, timers, backpressure, rescaling, and deterministic replay histories.

**RM-ANALYTICS-CONFORMANCE-0006:** Checkpoint/effect suites fail every barrier/state-storage/source-offset/sink-prepare/commit/ack boundary and verify declared at-most/at-least/exactly-once scope, fencing/idempotency, ambiguity reconciliation, and external nonclaims.

**RM-ANALYTICS-CONFORMANCE-0007:** Security/privacy suites probe row/field/function/source/sink isolation, side channels through errors/statistics/profiles/shuffle/spill/state/checkpoints, code/format/connector attacks, erasure, aggregation disclosure, and quotas.

**RM-ANALYTICS-CONFORMANCE-0008:** Migration/recovery suites cover mixed jobs/schemas/functions/connectors, savepoint migration, shadow comparison, rescaling, regional restore/failback, source reconstruction, sink reconciliation, and each declared reproducibility class.

**RM-ANALYTICS-CONFORMANCE-0009:** Provider reports publish unsupported semantics, emulations, weaker guarantees, configuration prerequisites, versions, conversion loss, resource/cost measurements, and waivers.
