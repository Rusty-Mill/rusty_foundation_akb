# Logical queries and expression semantics

**RM-ANALYTICS-LOGICAL-0001:** A logical plan is immutable and typed, binds resolved catalog/source generations, and represents scans, projections, filters, joins, aggregates, windows, sets, sorts, limits, unnesting, table functions, writes, and streaming operations without provider mechanics.

**RM-ANALYTICS-LOGICAL-0002:** Expression semantics define three-valued/null logic, missing values, type coercion, equality/order, collation, numeric overflow/rounding, floating behavior, time zone/calendar/DST, interval arithmetic, regex/pattern, collection/nested access, and error versus null behavior.

**RM-ANALYTICS-LOGICAL-0003:** Functions bind stable identity/version, signature/types, null/error behavior, determinism, volatility, side effects, authority, locale/time/randomness, resource limits, implementation/provider, and serialization compatibility.

**RM-ANALYTICS-LOGICAL-0004:** Nondeterministic values such as current time, random seeds, identity, and external lookups are captured once at a declared scope or explicitly remain volatile; retries cannot silently change reproducibility or effects.

**RM-ANALYTICS-LOGICAL-0005:** Query parameters are typed values separated from syntax and identifiers; identifier/function/provider selection uses separately authorized validated construction.

**RM-ANALYTICS-LOGICAL-0006:** Rewrites preserve result multiset/order, null/error, nondeterminism, authorization, side-effect, time, and approximation semantics; otherwise they require explicit equivalence policy and evidence.

**RM-ANALYTICS-LOGICAL-0007:** Result order is unspecified without a total ordering contract. Limits without deterministic ordering select an arbitrary valid subset and cannot support reproducible paging.
