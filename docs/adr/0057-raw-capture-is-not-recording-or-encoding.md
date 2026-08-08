# ADR-0057: Raw capture is not recording or encoding

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native capture stacks may deliver raw pixels, device-compressed samples, previews, processed photos, or encoded files through adjacent APIs. Combining them into one capture abstraction hides transformations, timing, buffer ownership, codec dependencies, persistence authority, and quality loss.

## Decision

The foundational capture stream delivers typed timed raw frames. Encoded device samples, preview presentation, still-photo processing, codecs, containers, recording, transport, and photo-library/filesystem storage are separate capabilities or services composed explicitly. Every transformation and authority boundary remains observable.

## Consequences

- Raw-frame consumers receive exact layout/color/timing/lifetime contracts.
- Recording profiles must select encoder, container, storage, and durability behavior.
- Providers cannot silently satisfy a raw request with decoded/re-encoded content.
