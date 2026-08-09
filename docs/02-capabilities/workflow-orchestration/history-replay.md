# History, replay, and determinism

**RM-WORKFLOW-HISTORY-0001:** History is append-only durable evidence with instance/run identity, monotonic event sequence or equivalent frontier, event/schema/type, payload reference, causation, generation, timestamp quality, integrity, and retention classification.

**RM-WORKFLOW-HISTORY-0002:** Replay consumes recorded time, random values, identifiers, activity/task outcomes, signals, version markers, and side-effect results and emits the same orchestration commands under the declared deterministic equivalence contract.

**RM-WORKFLOW-HISTORY-0003:** Replay never invokes external activities, sends messages, creates timers, calls providers, evaluates mutable policy, reads current configuration, or performs domain effects except through an explicit repair/simulation mode with no production authority.

**RM-WORKFLOW-HISTORY-0004:** Determinism failures identify definition/code/toolchain generation, history position, expected/actual command, nondeterministic input, compatibility rule, and quarantine/repair action without mutating committed history.

**RM-WORKFLOW-HISTORY-0005:** Snapshots/checkpoints are authenticated acceleration artifacts bound to history frontier and definition/state schema; recovery verifies and falls back to history replay when invalid or incompatible.

**RM-WORKFLOW-HISTORY-0006:** History compaction, archival, continue-as-new, and retention preserve audit/causality, deduplication, outstanding effects/tasks/timers, migration evidence, legal/privacy requirements, and restore capability or declare exact loss.
