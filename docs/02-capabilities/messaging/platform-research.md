# Messaging protocol and platform research

## Primary sources

- The official [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/), [deadlines](https://grpc.io/docs/guides/deadlines/), [cancellation](https://grpc.io/docs/guides/cancellation/), and [status](https://grpc.io/docs/guides/status-codes/) documentation distinguish unary/streaming calls, metadata, deadlines, cancellation, and locally observed termination.
- The official [Protocol Buffers language guide](https://protobuf.dev/programming-guides/proto3/) documents encoding-specific schema evolution, unknown fields, field-number reservation, presence, and unsafe or conditionally safe changes.
- [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html) defines link delivery state and settlement rather than a universal domain completion guarantee.
- [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) defines session/message expiry, QoS handshakes, acknowledgments, flow control, subscriptions, and reason codes within its protocol boundary.
- The [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) illustrates a portable event context separated from protocol bindings and payload schemas.

## Portability conclusion

Windows, Linux, and macOS provide transports and credential/storage primitives, not one native RPC or durable messaging semantic. Portable frameworks differ in schemas, code generation, deadline/cancellation behavior, flow control, retries, load balancing, broker settlement, transactions, observability, and platform support. Rusty Mill therefore standardizes semantic contracts and evidence while product RFCs select exact wire protocols, schema languages, brokers, generators, and compatibility policy.

