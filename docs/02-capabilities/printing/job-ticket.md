# Job ticket negotiation

A ticket is structured output intent. A resolved plan is the provider's immutable response for one document representation and destination generation.

**RM-PRINT-TICKET-0001:** Intent dimensions MUST distinguish required, preferred, permitted-default, prohibited, and unspecified values. User-selected values override product preferences only within product security and data-handling constraints.

**RM-PRINT-TICKET-0002:** Resolution MUST bind destination/capability generation, document identity/format, selected page set, copies/collation, media/source, orientation/scaling, sides, color/quality/resolution, finishings/output, accounting/release, interaction, and fidelity policy.

**RM-PRINT-TICKET-0003:** The result MUST report requested, effective, defaulted, substituted, ignored, unsupported, conflicting, and deferred values with reasons. Silent substitution is prohibited for required constraints.

**RM-PRINT-TICKET-0004:** Constraints are relational: support for each value independently does not prove that their combination is valid. The provider MUST resolve the whole ticket and revalidate it immediately before native submission.

**RM-PRINT-TICKET-0005:** Per-page or per-document overrides are optional and preserve scope/order. Providers that cannot express them reject or expose an explicit split-job/degradation plan; they MUST NOT silently flatten them.

**RM-PRINT-TICKET-0006:** Native opaque ticket extensions are namespaced, size-bounded, untrusted, non-authoritative, and opt-in. Portable code cannot branch on driver/vendor identity to infer semantics.

**RM-PRINT-TICKET-0007:** Interactive native print panels and headless/silent ticket resolution are separate services. A panel's acceptance produces intent/evidence, not capability authority or a submitted job.

See [ADR-0064](../../adr/0064-print-plans-bind-destination-generation-and-format.md).
