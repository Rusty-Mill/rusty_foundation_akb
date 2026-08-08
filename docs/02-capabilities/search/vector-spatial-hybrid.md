# Vector, spatial, and hybrid retrieval

**RM-SEARCH-VECTOR-0001:** A vector field binds embedding model and preprocessing generations, dimensionality, numeric encoding/quantization, normalization, distance/similarity, missing/invalid policy, index algorithm, and provenance.

**RM-SEARCH-VECTOR-0002:** Exact and approximate nearest-neighbor operations are different query modes. Approximate mode declares candidate/beam/probe/search parameters, filter order, recall objective, nondeterminism, fallback, and resource limits.

**RM-SEARCH-VECTOR-0003:** Embedding model changes create a new incompatible representation generation and use re-embedding/reindex and dual-query/fusion migration; vectors from different spaces are not compared silently.

**RM-SEARCH-VECTOR-0004:** Vector input is validated for dimension, finite values, norm, encoding, size, model/tenant authority, and adversarial resource use; raw embeddings are classified for privacy and inference risk.

**RM-SEARCH-SPATIAL-0001:** Spatial fields and queries bind coordinate reference system, axis order, units, dimensionality, geometry validity, antimeridian/pole behavior, precision, containment/boundary semantics, and approximation.

**RM-SEARCH-HYBRID-0001:** Hybrid search declares lexical/vector/spatial candidate depths, normalization/calibration, fusion algorithm/weights, filters, reranking stages, tie breakers, missing-signal behavior, and model/policy generations.

**RM-SEARCH-HYBRID-0002:** Candidate retrieval and reranking preserve attribution for each signal and stage; a final score never erases whether a hit was absent from another candidate set.

**RM-SEARCH-HYBRID-0003:** Learned rerankers bind model/features/training provenance, protected-attribute policy, prompt/input limits where applicable, nondeterminism, timeout/fallback, and offline/online evaluation.
