# Document source and representations

`rm.print.document-source` is an immutable generation-scoped resource that supplies bounded page descriptions or a declared encoded document. It does not expose application editing state or a printer driver API.

**RM-PRINT-DOCUMENT-0001:** A document descriptor MUST state identity/generation, title under privacy policy, ordered page count or bounded unknown-count policy, page boxes/units, orientation semantics, color intent, transparency/raster needs, resource policy, sensitivity, and reproducibility quality.

**RM-PRINT-DOCUMENT-0002:** Page indices, logical pages, selected page ranges, imposed sheets, sides/impressions, and physical sheets MUST remain distinct; counts always name their unit.

**RM-PRINT-DOCUMENT-0003:** A native/encoded representation MUST declare exact media type, format/version/profile where knowable, byte length or bound, seek/replay behavior, producer provenance, validation status, and external-resource/font dependencies.

**RM-PRINT-DOCUMENT-0004:** Rendering a page MUST use an immutable resolved output plan and declared page geometry. Repeated rendering under a deterministic claim produces equivalent semantic output and MUST NOT read ambient locale, time, configuration, identity, network, or mutable UI state.

**RM-PRINT-DOCUMENT-0005:** Font embedding/subsetting, image decoding, color profiles, links/annotations, metadata, transparency flattening, and external resource use follow explicit license, privacy, fidelity, and size policy.

**RM-PRINT-DOCUMENT-0006:** Producers and adapters treat document bytes, fonts, images, tickets, and device responses as untrusted. Parsing and rendering are bounded and preferably isolated for hostile formats.

PDF, XPS/OpenXPS, PWG/Apple raster, PostScript, PCL, and vendor formats are negotiated representations, not the portable domain model. A general graphics command model remains outside this slice.
