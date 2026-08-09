# Schemas and provider mappings

**RM-IDENTITY-GOV-MAPPING-0001:** Each adapter publishes a versioned mapping between the portable model and SCIM, LDAP, Windows, Linux, macOS, or service-native representations, including unsupported fields and operations.

**RM-IDENTITY-GOV-MAPPING-0002:** Mappings distinguish absent, null, empty, unknown, withheld, unsupported, defaulted, truncated, and malformed values; conversion never silently invents semantic equivalence.

**RM-IDENTITY-GOV-MAPPING-0003:** Identifier, case, normalization, uniqueness, mutability, cardinality, reference, time, binary, locale, and extension rules are preserved or reported as explicit loss.

**RM-IDENTITY-GOV-MAPPING-0004:** Writes preflight provider capabilities and bind expected target version where supported. Read-after-write or later reconciliation establishes observed state; a protocol success only proves its stated boundary.

**RM-IDENTITY-GOV-MAPPING-0005:** Product profiles explicitly select schemas, extensions, mapping generations, required round trips, conflict policy, provider quirks, and compatibility tests.
