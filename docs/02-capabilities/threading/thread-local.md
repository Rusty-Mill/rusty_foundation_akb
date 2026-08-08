# Thread-local state

**RM-THREAD-TLS-0001:** A thread-local key has process generation, initialization policy, destructor policy, and provider capacity. Values are scoped to native thread identity, not async task identity.

**RM-THREAD-TLS-0002:** Lazy initialization is reentrancy-safe or fails explicitly. Recursive initialization cannot observe a partially initialized safe value.

**RM-THREAD-TLS-0003:** Destructor invocation count/order, repeated setting during destruction, process termination, plugin unload, foreign threads, and forced exit vary; correctness cannot depend on destructor delivery.

**RM-THREAD-TLS-0004:** Thread-local state does not automatically propagate across spawned threads, pools, callbacks, async migration, IPC, or plugins. Correlation/security contexts use explicit propagation.

**RM-THREAD-TLS-0005:** Native TLS slots and destructor callbacks associated with unloadable code require generation/lifetime coordination; plugin retirement cannot assume all foreign threads have run destructors.

