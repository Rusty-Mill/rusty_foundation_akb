# Polyglots and interpretation conflicts

**RM-CONTENT-POLYGLOT-0001:** Inspection retains all credible interpretations and the byte regions each consumes. A later or higher-ranked match does not erase another valid parser view.

**RM-CONTENT-POLYGLOT-0002:** Conflicts include declaration/detection mismatch, multiple signatures, wrapper/payload disagreement, alternate parser profiles, appended/trailing content, overlapping objects, active content within passive types, and extension/application disagreement.

**RM-CONTENT-POLYGLOT-0003:** Security policy evaluates the most privileged credible interpretation available to any downstream consumer, proxy, browser, shell, office suite, media framework, package manager, or transformation pipeline in scope.

**RM-CONTENT-POLYGLOT-0004:** Parser differential tests bind exact provider/library/build and configuration. Agreement between two wrappers over the same parser is not independent evidence.

**RM-CONTENT-POLYGLOT-0005:** Normalization or transformation must either eliminate disallowed alternate interpretations under the target consumer set or report that it cannot. Changing a suffix or declared media type is not remediation.

**RM-CONTENT-POLYGLOT-0006:** Trailing, prepended, embedded, concatenated, and overlay data are accepted, preserved, stripped, or rejected only by an exact profile with loss and signed-view consequences.
