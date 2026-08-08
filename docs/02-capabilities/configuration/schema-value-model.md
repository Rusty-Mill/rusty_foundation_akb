# Schema and value model

## Capability identity

`rm.config.schema` defines the portable description and validation of configuration keys.

## Normative contract

**RM-CONFIG-SCHEMA-0001:** Every key has a stable namespaced identity, declared value type, default policy, validation constraints, sensitivity class, reload policy, and schema version history.

**RM-CONFIG-SCHEMA-0002:** Portable values are limited to explicitly modeled scalar, sequence, map, enum, duration, size, path, endpoint, and secret-reference types; conversion from native representations is validated and cannot silently truncate or coerce.

**RM-CONFIG-SCHEMA-0003:** A default is either a deterministic schema value or an explicit absence. Defaults that depend on locale, platform, hardware, time, network, or authority are computed by a named provider and expose that provenance.

**RM-CONFIG-SCHEMA-0004:** Unknown keys and known keys with invalid values are distinct diagnostics. Policy chooses whether unknown keys are rejected, warned, or retained as opaque migration input.

**RM-CONFIG-SCHEMA-0005:** Schema evolution may add optional keys and constraints that accept all previously valid values. Renames, removals, type changes, narrower constraints, precedence changes, and changed default meaning are breaking unless mediated by a declared migration.

**RM-CONFIG-SCHEMA-0006:** Validation is pure with respect to a supplied schema, candidate values, and explicit validation context. It performs no ambient I/O or secret disclosure.

## Reload classes

| Class | Meaning |
|---|---|
| Live | May enter a new active snapshot after successful validation |
| Coordinated | Requires a named service transaction before activation |
| Restart required | Reported as pending; active process behavior does not change |
| Immutable | Cannot change for the lifetime of the configured resource |

Cross-key constraints name all participating keys. A failed constraint rejects the candidate snapshot as a unit unless the schema explicitly defines an independent configuration partition.

