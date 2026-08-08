# State, checkpoints, and effect guarantees

**RM-ANALYTICS-STATE-0001:** Operator state binds job/operator/key/window/configuration generation, logical schema, serializer version, input frontier, timers, TTL, backend/storage, encryption, size, and rescaling ownership.

**RM-ANALYTICS-CHECKPOINT-0001:** A checkpoint coordinates exact participating tasks, input positions, in-flight record policy, operator state, timers/watermarks, sink preparations, topology/configuration generation, and durable manifest.

**RM-ANALYTICS-CHECKPOINT-0002:** Checkpoint completion proves only its named state/input/sink-preparation boundary; it does not prove every external effect, source retention, backup, result visibility, or business outcome.

**RM-ANALYTICS-EFFECT-0001:** At-most-once, at-least-once, and exactly-once claims name records/events, operator state, result identity, sources, sinks, failure/recovery model, replay horizon, and excluded external effects.

**RM-ANALYTICS-EFFECT-0002:** Exactly-once operator state may replay processing. End-to-end exactly-once effects require replayable sources plus atomic/transactional sinks, resource-enforced fencing, or durable idempotency/deduplication at the exact effect boundary.

**RM-ANALYTICS-EFFECT-0003:** Two-phase sink commits bind checkpoint/job/attempt generations, prepared resources, authority/fencing, timeout, recovery, abort, ambiguous coordinator outcomes, and external visibility.

**RM-ANALYTICS-CHECKPOINT-0003:** Aligned and unaligned checkpoints disclose backpressure/in-flight capture, size/latency/recovery tradeoffs, compatibility, and failure behavior.

**RM-ANALYTICS-STATE-0002:** State TTL/cleanup is processing policy, not a legal retention or complete erasure guarantee; expired state, checkpoints, savepoints, logs, sinks, and source data have separate lifecycles.
