# State, ordering, and recovery

The service tracks virtual keyboard keys, pointer buttons, touch/pen contacts, modifiers, lock assumptions, device generations, last accepted event, and uncertainty. State belongs to the participant's virtual device, not a process-global synthetic device.

**RM-REMOTE-INTERACTION-STATE-0001:** Press/down/start and release/up/end transitions MUST be validated as a state machine. Impossible, duplicate, missing, or cross-generation transitions MUST be rejected or reconciled explicitly.

**RM-REMOTE-INTERACTION-STATE-0002:** Events MUST carry participant/device sequence and batch/frame boundaries. Network order, arrival time, and sender timestamps are evidence, not an implicit total order.

**RM-REMOTE-INTERACTION-STATE-0003:** On loss, timeout, revocation, participant removal, focus/boundary change, or shutdown, the service MUST stop accepting new events and attempt bounded release/cancel of owned active state where native policy permits.

**RM-REMOTE-INTERACTION-STATE-0004:** Release/cancel acceptance MUST NOT be reported as proof that the target observed a clean state. Residual pressed/contact ambiguity is reported and may require local recovery guidance.

**RM-REMOTE-INTERACTION-STATE-0005:** Reconnect MUST create a new transport and virtual-device generation, begin from a neutral declared state, and discard late packets from all prior generations.

**RM-REMOTE-INTERACTION-STATE-0006:** Bounded queues MUST declare event-rate, burst, age, memory, coalescing, fairness, and overflow policies. Key/button/contact transitions cannot be coalesced as pointer motion.

**RM-REMOTE-INTERACTION-STATE-0007:** Shutdown completes only after admission closes, queued commands retire, release/cancel policy runs, native callbacks quiesce or detach safely, and final ambiguity is recorded.
