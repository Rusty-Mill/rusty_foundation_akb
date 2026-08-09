# Detection, probing, and confidence

**RM-CONTENT-DETECT-0001:** Detection requests bind purpose, candidate universe, provider/rule generation, allowed byte ranges and seeks, maximum bytes/time/work/memory, nested-inspection policy, declared evidence, and ambiguity threshold.

**RM-CONTENT-DETECT-0002:** A finding names candidate identity/profile, matched rule/signature/structure, exact offsets/ranges, required and absent checks, contradictions, specificity, confidence class defined by that provider, and remaining ambiguity.

**RM-CONTENT-DETECT-0003:** Numeric confidence is not portable probability. Providers publish calibration and candidate-set semantics; policy uses named evidence thresholds rather than comparing unrelated scores.

**RM-CONTENT-DETECT-0004:** Magic bytes alone prove only a matched pattern. Structure validation incrementally checks lengths, offsets, checksums, object graphs, mandatory fields, terminators, and profile constraints without constructing active domain objects.

**RM-CONTENT-DETECT-0005:** Detection is bounded and monotonic in evidence but not necessarily in conclusion: additional bytes may refine, contradict, or reveal a wrapper/polyglot. Early results carry required-more-data and terminality evidence.

**RM-CONTENT-DETECT-0006:** Stream detection never consumes irrecoverable bytes invisibly. It returns replayable buffered prefix ownership, advances only under caller agreement, or requires a seekable source.

**RM-CONTENT-DETECT-0007:** Unknown and ambiguous are successful evidence outcomes; fallback to generic binary/text is explicit and cannot enable a more privileged handler.
