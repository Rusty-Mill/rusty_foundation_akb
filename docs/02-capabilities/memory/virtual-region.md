# Virtual region and backing model

## Capability identity

`rm.memory.virtual-region` owns a page-aligned virtual-address range and its declared backing state.

**RM-MEMORY-REGION-0001:** Creation specifies requested length, alignment, placement policy, initial accessibility, backing/commit policy, inheritance, guard policy, and authority. Effective base, usable length, page/granularity facts, and quality are returned.

**RM-MEMORY-REGION-0002:** Reserved, backed/committed, resident, locked, dirty, discardable, and accessible are independent states. Providers cannot infer one from another or claim physical memory ownership.

**RM-MEMORY-REGION-0003:** Size and address arithmetic is checked before native calls. Rounding to page/allocation granularity is disclosed, and guard/metadata ranges are excluded from safe usable views.

**RM-MEMORY-REGION-0004:** Commit/backing and decommit/discard operate on aligned subranges and report exact resulting state. Partial success is prohibited unless the result enumerates each affected interval.

**RM-MEMORY-REGION-0005:** Releasing a region invalidates all derived addresses and views. Safe APIs tie borrow lifetime to the region and prevent access during incompatible protection/remap transitions.

**RM-MEMORY-REGION-0006:** Requested fixed placement is an advanced unsafe/authority-sensitive quality. Failure never silently replaces an existing mapping, and ordinary allocation lets the OS select randomized placement.

**RM-MEMORY-REGION-0007:** Allocation failure distinguishes address-space exhaustion, backing/commit limit, permission/policy denial, alignment/size invalidity, unsupported flags, and provider/resource failure where evidence permits.

