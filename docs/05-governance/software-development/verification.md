# Testing, conformance, fuzzing, and failure evidence

**RM-DEV-TEST-0001:** Non-trivial logic has happy-path, failure, boundary, and invariant tests. Concurrency, cancellation, partial effects, cleanup, recovery, evolution, hostile input, and overload tests apply where the contract exposes those risks.

**RM-DEV-TEST-0002:** Tests trace to semantic assertions and normative requirements; harness cases keep separate stable identities. Passing tests cannot establish claims outside their bound provider/platform/environment/oracle.

**RM-DEV-TEST-0003:** Unit tests isolate deterministic logic; integration tests cover real boundaries; conformance suites remain backend-neutral; provider tests capture native evidence; end-to-end tests validate selected profile composition without replacing lower-level diagnostics.

**RM-DEV-TEST-0004:** Property/model tests cover algebraic, state-machine, ordering, serialization, and concurrency invariants. Seeds, schedules, minimized counterexamples, and model versions are retained.

**RM-DEV-TEST-0005:** Parsers, decoders, protocol/state machines, unsafe adapters, archive/media handlers, and security boundaries have fuzz plans with corpora, dictionaries, resource limits, sanitizers/interpreters where applicable, crash deduplication, and regression fixtures.

**RM-DEV-TEST-0006:** Tests MUST be hermetic or explicitly classify external dependencies. Time, randomness, locale, environment, network, filesystem, identity, and provider state are injected/controlled where determinism matters.

**RM-DEV-TEST-0007:** A flaky result is failure evidence, not pass. Quarantine requires owner, bounded scope, issue, expiry, retained failure artifacts, and prohibition on affected release claims.

**RM-DEV-TEST-0008:** Platform matrices cover every claimed Windows, Linux, and macOS target/provider plus declared architecture/toolchain variants. Emulators/simulators cannot silently replace required physical/native evidence.

**RM-DEV-TEST-0009:** Failure bundles minimize sensitive data and include source/artifact digests, assertion/case IDs, environment, configuration, seed/schedule, normalized observations, logs/traces, and reproduction steps.

**RM-DEV-TEST-0010:** Coverage metrics guide risk review but cannot replace requirement traceability, meaningful oracles, mutation/fault evidence, or reviewer judgment.
