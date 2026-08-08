# Progressive, tiled, and region decode

**RM-IMAGE-PROGRESS-0001:** Incremental input reports consumed/retained byte ranges, seek requirements, completeness, discovered structure changes, next useful input, and terminal status. End-of-current-input and end-of-stream are distinct.

**RM-IMAGE-PROGRESS-0002:** A progressive/interlaced preview is an immutable provisional revision with level/pass, valid region, quality/completeness class, source-byte frontier, replaced revision, and final/non-final status.

**RM-IMAGE-PROGRESS-0003:** Consumers MUST replace rather than mutate published revisions and MUST NOT persist, export, authenticate, or treat a provisional preview as final without explicit product policy and labeling.

**RM-IMAGE-REGION-0001:** Region/tile decode binds requested coordinates to stored, oriented, or display space; effective expanded region, codec block alignment, scale level, halo/dependency area, and returned geometry are reported.

**RM-IMAGE-REGION-0002:** Native reduced-resolution or region decode is a quality claim. A provider that decodes the full image and crops/scales afterward discloses memory/time cost and cannot satisfy a strict bounded-region requirement.

**RM-IMAGE-REGION-0003:** Sparse, pyramidal, tiled, multi-resolution, and remotely fetched sources use bounded tile caches keyed by exact source/item/level/region/description/decoder generation with loss and retry policy.

**RM-IMAGE-PROGRESS-0004:** Progressive updates are coalesced/backpressured by explicit policy. Malicious streams cannot force unbounded revisions, repeated whole-frame allocation, UI invalidation, or quadratic reconstruction.
