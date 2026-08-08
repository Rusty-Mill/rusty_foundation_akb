# Streaming interactions

**RM-MESSAGING-STREAM-0001:** Streaming kind declares client/server/bidirectional message directions, ordered scope, half-close rules, response/status placement, message schemas, maximum in-flight messages/bytes/time, and independent send/receive cancellation semantics.

**RM-MESSAGING-STREAM-0002:** A message stream preserves typed message boundaries above a bounded framing codec; it is not an arbitrary byte stream. Headers, message length, compression flag, content, trailers/status, and partial/truncated framing are validated incrementally.

**RM-MESSAGING-STREAM-0003:** Send readiness, enqueue, framing, transport flow-control, peer receive, application consumption, acknowledgment, and effect are separate. Backpressure propagates across handler, codec, protocol, transport, and storage without unbounded buffering or deadlocking unrelated streams.

**RM-MESSAGING-STREAM-0004:** Bidirectional directions are concurrent and independently half-closable. Implementations cannot assume lockstep request/response, symmetric progress, or that receiving terminal status means every outbound message was consumed.

**RM-MESSAGING-STREAM-0005:** Per-message and stream-wide compression declare algorithms, context reuse, sensitive-content separation, input/output/ratio/memory/time bounds, flush behavior, and failure scope. Decompression failure cannot expose a message as complete.

**RM-MESSAGING-STREAM-0006:** Stream cancellation/reset reports last locally accepted/sent/received/delivered message identities and byte progress, peer knowledge quality, buffered residuals, handler/domain state, and whether the containing session remains usable.

**RM-MESSAGING-STREAM-0007:** Resume is an application protocol with generation, cursor/sequence, acknowledgment semantics, retention, snapshot, gap/overlap/duplicate policy, and authorization. Reopening a transport stream does not resume a logical stream automatically.

