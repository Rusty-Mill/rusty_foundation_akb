# Aggregation, rating, allocation, and correction

**RM-TENANT-GOV-RATING-0001:** Aggregation declares sum/count/max/min/last/distinct/time-weighted/tiered semantics, grouping dimensions, inclusive start/exclusive end periods, time zone/calendar, late window, rounding, precision, and reset behavior.

**RM-TENANT-GOV-RATING-0002:** Aggregates retain source frontier, meter/schema generation, input count/digest, deduplication state, window, completeness/late status, calculation version, and reproducibility evidence.

**RM-TENANT-GOV-RATING-0003:** Rating is a separate pure derivation over qualified usage, price/tier/commitment/discount/tax-input generations, currency/precision, period, and policy; usage quantity is not cost.

**RM-TENANT-GOV-RATING-0004:** Allocation/showback/chargeback labels and rules preserve total reconciliation, shared-cost method, unallocated residual, split rationale, and source charge identity without mutating raw usage.

**RM-TENANT-GOV-RATING-0005:** Corrections, credits, reversals, rerating, late usage, and dispute resolutions create immutable adjustment records referencing displaced inputs/results and effective/accounting periods.

**RM-TENANT-GOV-RATING-0006:** Closed-period restatement policy distinguishes operational corrected usage, customer-facing adjustment, invoice amendment/credit, and accounting treatment; the architecture makes no accounting conclusion.
