# Definitions, state machines, and validation

**RM-WORKFLOW-DEFINITION-0001:** A definition binds stable workflow type, immutable generation/digest, input/output/state/event/activity/task schemas, states/nodes/transitions, conditions, timers, retries, compensation, cancellation, child boundaries, limits, compatibility, and provenance.

**RM-WORKFLOW-DEFINITION-0002:** State-machine, DAG, sequence, choice, loop, parallel/map, event race, subworkflow, and ad-hoc/human constructs retain exact join, ordering, cardinality, completion, error, and cancellation semantics rather than being normalized into generic nodes.

**RM-WORKFLOW-DEFINITION-0003:** Validation detects unreachable states, missing terminal paths, unbounded loops/fan-out/history growth, ambiguous transitions, inconsistent joins, timer/calendar gaps, event correlation collisions, unsupported compensation, schema incompatibility, and nondeterministic expressions.

**RM-WORKFLOW-DEFINITION-0004:** Expressions/functions declare type, null/error behavior, purity, determinism, version, resource bounds, locale/time/calendar, allowed state/input access, and migration compatibility.

**RM-WORKFLOW-DEFINITION-0005:** Definition publication binds toolchain/compiler, validation and replay tests, simulation, approvals, signature/provenance, activation scope/time, predecessor, compatibility declaration, rollout, and rollback plan.

**RM-WORKFLOW-DEFINITION-0006:** Visual notation and executable semantics are linked by stable element identifiers and validation; diagram layout, labels, lanes, or informal annotations cannot silently change execution meaning.
