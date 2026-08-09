# Provider evidence, outcomes, and reconciliation

**RM-COMMS-OUTCOME-0001:** Provider requests/responses/webhooks are authenticated, schema/version bound, idempotently recorded, ordered only within declared scope, and resilient to duplicate, delay, gaps, replay, unknown fields, and provider status regression.

**RM-COMMS-OUTCOME-0002:** Status mappings preserve native provider/channel value, normalized milestone, claimed boundary, confidence, event/observation times, terminality, and loss; unsupported evidence remains unknown.

**RM-COMMS-OUTCOME-0003:** Periodic reconciliation reads provider source state/cursors and compares local attempts, callbacks, suppressions, charges, and unknowns. Callback absence is not proof of non-delivery.

**RM-COMMS-OUTCOME-0004:** Hard/soft bounce, block, deferral, mailbox full, invalid recipient, spam complaint, carrier rejection, invalid token, expired, collapsed, throttled, and provider failure retain distinct retry/suppression/routing policy.

**RM-COMMS-OUTCOME-0005:** Open, impression, click, read, reply, conversion, and unsubscribe events bind tracking method and uncertainty, deduplicate bots/proxies only under declared heuristics, and never become security or legal proof alone.

**RM-COMMS-OUTCOME-0006:** Provider cost/segment/route evidence maps to tenant metering separately from delivery status and is adjusted rather than rewritten when providers correct it.

**RM-COMMS-OUTCOME-0007:** Operational dashboards show planned/eligible/suppressed/attempted/accepted/handed-off/delivered/failed/unknown/engaged denominators and confidence without funnel arithmetic that silently drops unknown populations.
