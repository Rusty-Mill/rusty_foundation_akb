# Collation and localized search

**RM-I18N-COLLATE-0001:** A collator binds locale/context, usage (`sort` or `search`), strength, normalization, numeric ordering, case/alternate handling, script reordering, tailoring, and exact Unicode/CLDR/provider data versions.

**RM-I18N-COLLATE-0002:** Comparison defines a total ordering only within one exact collator contract. Results and sort keys are not compared across differing contexts/versions.

**RM-I18N-COLLATE-0003:** Collation equality is not byte/scalar identity, security equivalence, filesystem equality, identifier equality, or authorization. Stable identifiers use domain-defined canonical representation.

**RM-I18N-COLLATE-0004:** Sort keys include or are stored beside collator identity/version and are invalidated/rebuilt after relevant data/policy upgrades.

**RM-I18N-COLLATE-0005:** Localized search declares boundary, canonical/case/diacritic/width/punctuation/numeric handling, language tailoring, match ranges in semantic text units, and false-positive/negative limitations.

**RM-I18N-COLLATE-0006:** Search/collation of untrusted large text is bounded for CPU/memory and cannot trigger ambient locale/resource changes.

