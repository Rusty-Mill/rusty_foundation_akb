# HTTP streaming, backpressure, cancellation, and failure

**RM-HTTP-STREAM-0001:** Request and response content are bounded backpressured byte streams. Buffer-all, rewind, clone, compression, decompression, integrity verification, and representation decoding require separate policy and resource budgets.

**RM-HTTP-STREAM-0002:** Backpressure propagates across application, codec, HTTP flow-control, secure-channel, transport, and storage boundaries without holding unrelated connection-wide capacity indefinitely.

**RM-HTTP-STREAM-0003:** Expect/continue, informational response, request-body production, response-head arrival, response-body delivery, trailers, and exchange completion are separate milestones.

**RM-HTTP-STREAM-0004:** Cancellation reports locally-not-started, head-may-have-been-sent, content partially/fully sent, response observed, stream reset/connection closed, peer receipt unknown, and origin effect unknown as applicable.

**RM-HTTP-STREAM-0005:** HTTP/1.1 connection loss can make message boundaries and reuse unsafe; HTTP/2 and HTTP/3 stream resets can isolate a stream while connection errors affect all streams. Failure mapping retains the native scope.

**RM-HTTP-STREAM-0006:** Decompression and decoding enforce compressed/uncompressed byte, ratio, nesting, time, memory, and output limits. Integrity failure never exposes content as successfully complete.

