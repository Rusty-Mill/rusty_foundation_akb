# Structured event and schema model

## Capability identity

`rm.observe.event` emits immutable structured operational events.

**RM-OBSERVE-EVENT-0001:** Every event has a stable namespaced schema identity and version, severity/class, occurrence timestamp, emitting component identity, execution-instance identity, and typed fields.

**RM-OBSERVE-EVENT-0002:** Event fields declare type, unit, cardinality intent, sensitivity class, optionality, and compatibility history. Free-form message text cannot replace fields required for correlation, filtering, aggregation, or conformance.

**RM-OBSERVE-EVENT-0003:** Event creation never reads ambient correlation, locale, user identity, configuration, or authority. Such context is supplied explicitly or omitted with a diagnostic reason.

**RM-OBSERVE-EVENT-0004:** Schema evolution may add optional fields and enum values only where unknown-value handling is defined. Removing fields, changing meaning/type/unit/sensitivity, or reusing an identity is breaking.

**RM-OBSERVE-EVENT-0005:** Rendering is localized only at a user-facing presentation boundary. Persisted event identity, field names, numeric values, and canonical interchange remain locale independent.

**RM-OBSERVE-EVENT-0006:** Emission has a nonblocking bounded path. An event can be accepted, filtered, sampled, dropped, or rejected with aggregate loss accounting; application success cannot depend on exporter availability unless an explicit audit contract says otherwise.

## Event classes

Diagnostic logs, audit records, lifecycle events, measurements, span events, and crash breadcrumbs are distinct schema classes. Audit durability and access policy are separate optional quality claims; ordinary diagnostic logging cannot claim audit completeness.

