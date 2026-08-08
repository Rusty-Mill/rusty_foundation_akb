# ADR-0110: Watermarks are progress assertions, not completeness proof

## Status

Accepted

## Context

Stream processors use watermarks to advance event-time timers, close windows, emit results, and reclaim state despite out-of-order and delayed inputs. Watermarks derive from configured source observations, partition combination, idleness, and heuristics. Sources can violate assumptions, partitions can reappear, clocks and extraction can be wrong, and late records can still arrive. Treating a watermark as proof of complete history causes silent loss and false finality.

## Decision

Rusty Mill models each watermark as a monotonic progress assertion scoped to exact source partitions and a versioned generation/combination/idleness policy. It authorizes configured timer, emission, and state-retention decisions, not a universal claim that earlier events do not exist. Late-event handling, corrections/retractions, audit, and recovery remain explicit.

## Consequences

- Window finality is policy-qualified and evidence-bearing.
- State bounds and latency can be selected without hiding data-loss tradeoffs.
- Recovered or newly discovered partitions reconcile against prior progress.
- Product completeness claims require stronger source-specific evidence.
