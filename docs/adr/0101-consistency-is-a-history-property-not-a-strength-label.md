# ADR-0101: Consistency is a history property, not a strength label

## Status

Accepted

## Context

Terms such as strong consistency, eventual consistency, ACID, quorum read, and leader read are routinely used without naming operations, transaction boundaries, real-time order, replicas, sessions, caches, partitions, or allowed anomalies. Different systems use the same label for materially different histories, making portability and conformance claims untestable.

## Decision

Every Rusty Mill consistency claim names the object and operation model, invocation/response and commit boundaries, client/session/transaction scope, configuration/replicas, real-time/causal/session ordering, staleness and clock assumptions, failure model, and permitted histories/anomalies. Conformance captures concurrent histories under faults and checks the declared property. Unqualified strength labels are prohibited.

## Consequences

- Applications select semantics based on actual invariants rather than vendor vocabulary.
- Read results carry enough version/path/freshness evidence for safe use.
- Stronger semantics can cost more and remain explicit workload choices.
- Some provider guarantees remain unknown until experimentally or formally substantiated.

