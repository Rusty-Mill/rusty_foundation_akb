# Readiness and completion

Completion states that one requested operation reached a terminal result. Readiness states only that retrying some operation on a resource might make progress without blocking under the observed conditions.

**RM-ASYNC-ENGINE-0001:** Portable consumer contracts MUST be completion-oriented. A readiness provider MUST translate readiness plus bounded syscall attempts into operation completions.

**RM-ASYNC-ENGINE-0002:** Readiness MUST be treated as a level/edge/source-specific hint whose meaning, one-shot behavior, rearm rule, and error/hangup interaction are adapter concerns.

**RM-ASYNC-ENGINE-0003:** A provider MUST drain or rearm native readiness according to its selected mode and MUST tolerate stale, duplicated, coalesced, and concurrently consumed readiness.

**RM-ASYNC-ENGINE-0004:** A would-block result after readiness is not an error or completion; it returns the operation to pending without busy-spinning.

**RM-ASYNC-ENGINE-0005:** Native completion dequeue order, submission order, wake order, and consumer poll order MUST NOT be represented as equivalent unless a domain contract proves ordering.

**RM-ASYNC-ENGINE-0006:** Provider emulation using bounded blocking workers MUST be disclosed with thread, cancellation, shutdown, and saturation quality; it cannot claim native nonblocking quality.

See [ADR-0052](../../adr/0052-portable-asynchronous-io-is-completion-oriented.md).
