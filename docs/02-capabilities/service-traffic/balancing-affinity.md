# Load-balancing algorithms and affinity

**RM-TRAFFIC-BALANCE-0001:** Balancing policy declares eligible set, weights, priority/locality, algorithm/version, state scope, load signal, connection/request unit, slow-start, panic/fallback, randomness, and update behavior.

**RM-TRAFFIC-BALANCE-0002:** Round-robin, weighted random, least-request/load, power-of-N, consistent/rendezvous hash, ring, latency-aware, adaptive, and provider algorithms disclose assumptions, bias, convergence, stale state, complexity, and failure behavior.

**RM-TRAFFIC-BALANCE-0003:** Static discovery weight, configured route weight, capacity, active-request count, latency, queue, utilization, and application load are distinct signals with freshness, provenance, normalization, and trust.

**RM-TRAFFIC-BALANCE-0004:** Per-connection balancing can concentrate multiplexed requests/streams; protocols expose whether selection occurs per connection, request, stream, transaction, or session and how pools react to endpoint changes.

**RM-TRAFFIC-AFFINITY-0001:** Affinity binds key source and privacy, service/subset/policy generation, endpoint identity, lifetime, failover, rebalancing, tamper protection, and impact on fairness/load/fault tolerance.

**RM-TRAFFIC-AFFINITY-0002:** Cookie/header/token/source-address/application/session affinity are different mechanisms; client-controllable keys are validated and cannot escape authorized subsets or tenants.

**RM-TRAFFIC-BALANCE-0005:** Endpoint addition/removal, weight/capacity change, outlier state, locality loss, and rescaling update balancer state without unbounded remapping, synchronized reconnect storms, or stale endpoint resurrection.

**RM-TRAFFIC-BALANCE-0006:** Fairness is qualified across endpoints, tenants, priorities, connection lengths, request costs, and time; equal request counts do not imply equal load.
