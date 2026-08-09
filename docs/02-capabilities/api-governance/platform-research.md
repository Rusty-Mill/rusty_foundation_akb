# Platform and standards research

Research informs bindings; it does not replace Rusty Mill's logical model.

- [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html) describes HTTP operations, reusable components, callbacks, and incoming webhooks. It is a protocol description, not a universal behavioral-compatibility policy.
- [AsyncAPI Specification 3.0.0](https://www.asyncapi.com/docs/reference/specification/v3.0.0) describes application operations and channels for event-driven APIs.
- [Protocol Buffers proto3 guide](https://protobuf.dev/programming-guides/proto3/#updating) distinguishes wire-safe, unsafe, and conditionally compatible changes and requires care with removed field numbers/names; source and behavioral compatibility can still differ.
- [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) defines HTTP problem details; domain error identity and disclosure policy remain above that binding.
- [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) defines the HTTP `Deprecation` response header and composes with the [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) `Sunset` header. These communicate lifecycle state; they do not prove consumer migration.

## Research conclusions

**RM-API-GOV-RESEARCH-0001:** Rusty Mill keeps logical operations independent of description format so multiple protocols can compose without making one format the domain model.

**RM-API-GOV-RESEARCH-0002:** Standards-defined compatibility claims are preserved at their exact scope and never promoted to universal consumer compatibility.
