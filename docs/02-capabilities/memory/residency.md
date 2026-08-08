# Residency, locking, and discard

**RM-MEMORY-RESIDENCY-0001:** Prefault/populate, access-pattern advice, discard, page-out request, locking/wiring, large-page preference, and no-dump are independent optional operations with provider quality and range alignment.

**RM-MEMORY-RESIDENCY-0002:** A successful lock/wire claim states quota scope, inheritance, future-page behavior, revocation/resource-pressure behavior, and whether it prevents paging, swap, compression, or only eviction under the native platform.

**RM-MEMORY-RESIDENCY-0003:** Locking and no-dump do not cover prior/future copies, compiler temporaries, registers, devices, crash tools, hibernation, privileged access, or application-created files. They never prove secret containment.

**RM-MEMORY-RESIDENCY-0004:** Discard means contents may become unspecified/zero/reloaded according to the exact backing contract. Consumers cannot read discarded bytes until reinitialization is established.

**RM-MEMORY-RESIDENCY-0005:** Large/huge pages are negotiated by size, explicit-versus-transparent mode, privilege, fallback, fragmentation cost, and accounting. Silent fallback is disclosed and cannot satisfy a required large-page quality.

**RM-MEMORY-RESIDENCY-0006:** Memory-pressure observations are hints with platform provenance, not guaranteed predictors or authorization to discard durable/user data.

