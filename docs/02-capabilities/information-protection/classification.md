# Classification evidence and inference

**RM-PROTECTION-CLASSIFY-0001:** Assignment method is explicit: manual, mandatory user choice, default, inherited, rule-based automatic, model-based automatic, service-side, client-side, repository-side, import mapping, or administrator correction.

**RM-PROTECTION-CLASSIFY-0002:** Classifier input binds exact subject generation and inspected frontier, schema/fields/content/ranges, context/lineage, language/locale, tenant, rule/model/dictionary and provider generations, thresholds, limits, privacy mode, and purpose.

**RM-PROTECTION-CLASSIFY-0003:** Findings identify matched sensitive-information type/rule/model class, location and count/range, confidence class/calibration, supporting and contradictory evidence, exclusions, partial/opaque regions, and recommended labels without exposing sensitive values by default.

**RM-PROTECTION-CLASSIFY-0004:** Recommendation, automatic assignment, and enforcement are separate policies. A classifier cannot grant itself label-issuer, downgrade, encryption, sharing, or channel-block authority.

**RM-PROTECTION-CLASSIFY-0005:** Numeric confidence is provider/model scoped and does not compare across classifiers without calibration. Low confidence, no match, unsupported format, encrypted content, truncation, timeout, or scanner failure are distinct outcomes, not “not sensitive.”

**RM-PROTECTION-CLASSIFY-0006:** Manual classification captures principal, policy visibility, informed choice, optional justification, and subject generation. User choice may be policy-constrained but is not presumed accurate or malicious.

**RM-PROTECTION-CLASSIFY-0007:** Reclassification pins previous assertions and explains added, retained, superseded, conflicted, or removed evidence; background rescans cannot silently downgrade an existing assertion.
