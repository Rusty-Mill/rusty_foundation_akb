# Coordination protocol and platform research

## Primary sources

- [In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf) separates leader election, log replication, safety, membership change, and state-machine application in Raft.
- The official [etcd concurrency API](https://etcd.io/docs/v3.6/dev-guide/api_concurrency_reference_v3/) exposes sessions, leases, mutexes, elections, and leadership revisions while relying on the application's correct use of returned evidence.
- The Apache ZooKeeper [recipes and solutions](https://zookeeper.apache.org/doc/current/recipes.html) describe ephemeral/sequential-node patterns for locks, election, barriers, queues, and failure recovery.
- Google's [Spanner paper](https://research.google.com/archive/spanner-osdi2012.pdf) and [TrueTime/external-consistency documentation](https://cloud.google.com/spanner/docs/true-time-external-consistency) illustrate explicit clock-uncertainty bounds and precisely named transaction/read guarantees.

## Portability conclusion

Windows, Linux, and macOS provide local clocks, synchronization, files, networking, and process lifecycle—not a portable distributed quorum or consistency guarantee. Coordination providers differ in algorithms, storage, clocks, leases, fencing tokens, watches, transactions, consistency, membership, recovery, and managed-service controls. Rusty Mill standardizes explicit workloads and evidence; product RFCs select and validate a provider/protocol/topology against their failure model.

