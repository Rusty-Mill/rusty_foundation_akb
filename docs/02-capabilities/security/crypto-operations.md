# Operations, buffers, concurrency, and failure

**RM-CRYPTO-OP-0001:** Operation inputs MUST use exact byte semantics and checked lengths; localized text, implicit string encoding, C-string termination, platform integer layout, and mutable shared buffers are prohibited at the boundary.

**RM-CRYPTO-OP-0002:** Output sizing, caller/provider allocation, initialization, ownership, secret classification, memory domain, lifetime, zeroization claim, and behavior after failure/cancellation MUST be explicit.

**RM-CRYPTO-OP-0003:** Key handles and operation contexts MUST declare thread safety, reentrancy, clone/share behavior, serialization, maximum concurrency, and provider affinity. Locks MUST NOT be held across interactive or remote provider calls without bounded design.

**RM-CRYPTO-OP-0004:** Async operations expose queued, provider-started, interaction-required, executing, result-ready, canceled-requested, and terminal milestones. Cancellation does not prove hardware/remote work or key-use accounting was undone.

**RM-CRYPTO-OP-0005:** Errors MUST distinguish invalid input/encoding, policy rejection, wrong key/usage, authentication/signature invalidity, interaction/permission denial, key unavailable/revoked/expired, provider/self-test failure, resource/rate limit, cancellation, partial/unknown outcome, and unsupported operation without exposing an oracle to untrusted peers.

**RM-CRYPTO-OP-0006:** Sensitive temporary material, plaintext, shared secrets, derived keys, nonces/counters, and provider buffers MUST have a documented exposure/copy/swap/dump/zeroization map. Zeroization is scoped evidence, not proof of physical erasure.

**RM-CRYPTO-OP-0007:** Constant-time and side-channel claims MUST identify operation, secret-dependent inputs, provider/compiler/hardware/configuration, leakage model, measurement/review evidence, and excluded channels. No portable blanket claim is allowed.

**RM-CRYPTO-OP-0008:** Sync paths are complete but use bounded waits over the same operation state, preserve prompt/thread affinity, and cannot create hidden runtimes or block realtime/UI contexts indefinitely.
