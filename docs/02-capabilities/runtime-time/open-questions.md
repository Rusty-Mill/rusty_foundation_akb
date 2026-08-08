# Runtime and time open questions

**Status:** Active register

| ID | Question | Why it matters | Evidence or decision needed |
|---|---|---|---|
| RT-Q001 | Is continuous monotonic time mandatory? | Profiles may rely on suspend-inclusive deadlines. | Platform/version availability and workload scenarios |
| RT-Q002 | Which Windows clock pair best preserves active and continuous semantics? | QPC, unbiased interrupt time, and tick/interrupt time have different precision and suspend behavior. | Prototype measurements and supported-version policy |
| RT-Q003 | Are periodic timers a capability or service? | Missed ticks, drift, burst catch-up, and coalescing introduce policy. | Scenario analysis |
| RT-Q004 | What is the maximum guaranteed timer scale? | Backend designs differ between OS timers and aggregated logical timers. | Benchmark prototype |
| RT-Q005 | Are cancellation callbacks normative? | They add reentrancy, panic, ordering, and allocation concerns. | Two consumer designs and concurrency review |
| RT-Q006 | ~~Is orderly shutdown a capability or platform service?~~ **Closed: platform service.** | It coordinates other capabilities and policy. | [ADR-0005](../../adr/0005-orderly-shutdown-is-a-platform-service.md) |
| RT-Q007 | What precision-reduction policies are required? | High-resolution time affects privacy and side channels. | Security/privacy threat model |
| RT-Q008 | What should happen when a continuous deadline passes during suspend? | Delivery after resume differs from waking the machine. | Profile scenarios and power-policy review |
| RT-Q009 | What minimum OS versions are supported? | Changes native mechanism availability and fallback needs. | Ecosystem support policy RFC |
| RT-Q010 | How are virtualized clocks tested? | CI runners and containers may expose discontinuities or unusual resolution. | Test-lab design |

Questions are closed only by linking an ADR, accepted RFC section, conformance result, or platform evidence. Closed identifiers are never reused.
