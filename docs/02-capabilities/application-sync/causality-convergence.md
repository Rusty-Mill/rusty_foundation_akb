# Causality, ordering, and convergence

**RM-APP-SYNC-CAUSAL-0001:** Ordering claims declare object/dataset/partition/session scope and distinguish causal precedence, concurrency, provider sequence, total order, wall time, and presentation order.

**RM-APP-SYNC-CAUSAL-0002:** Vector clocks, version vectors, dotted contexts, Lamport clocks, hybrid clocks, and provider revisions are mapped with exact actor/incarnation, compare, merge, truncation, trust, privacy, and overflow semantics.

**RM-APP-SYNC-CAUSAL-0003:** Wall-clock timestamps alone cannot prove causal order. Clock-based tie-breaking declares clock source, skew bounds, malicious/failed clock behavior, stable secondary order, and semantic loss.

**RM-APP-SYNC-CAUSAL-0004:** A convergence claim names eligible replicas, delivered change set/frontier, quiescence or ongoing-update assumption, merge algebra, schema/policy generation, authority, and deadline/objective.

**RM-APP-SYNC-CAUSAL-0005:** Strong eventual convergence requires equivalent changes and causal context plus deterministic/convergent application; equal visible bytes alone do not prove equal hidden metadata or future behavior.

**RM-APP-SYNC-CAUSAL-0006:** Causal metadata compaction proves retired actors and obsolete dots cannot return. Approximation or truncation is disclosed and cannot silently strengthen ordering claims.
