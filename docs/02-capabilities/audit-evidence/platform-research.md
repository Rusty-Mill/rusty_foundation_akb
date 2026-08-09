# Platform and standards research

- NIST [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) provides enterprise computer-security log-management guidance; [SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) includes Audit and Accountability controls, while [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) defines assessment procedures.
- [RFC 5424](https://www.rfc-editor.org/rfc/rfc5424.html) defines structured Syslog including distinct timestamp quality; [RFC 5848](https://www.rfc-editor.org/rfc/rfc5848.html) adds origin authentication, integrity, replay resistance, sequencing, and missing-message detection within its scope.
- [RFC 3161](https://www.rfc-editor.org/rfc/rfc3161.html) defines cryptographic time-stamp tokens over data imprints; timestamps do not establish claim truth.
- W3C [PROV-O](https://www.w3.org/TR/prov-o/) models entities, activities, agents, derivation, attribution, and provenance-of-provenance for interoperable evidence relationships.
- OpenTelemetry's stable [Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) distinguishes source timestamp, observed timestamp, severity, body, resource, instrumentation scope, trace context, and attributes.
- NIST OSCAL's [Assessment Results model](https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/) represents assessment scope, activities, observations/evidence, findings, risks, and attestations in machine-readable forms.
- AWS CloudTrail's [log integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) illustrates digest/signature chaining and the crucial distinction between enabling proof generation and actually validating a range.

**RM-AUDIT-RESEARCH-0001:** Rusty Mill maps native/provider logs and assessment formats loss-consciously without treating transport schemas as the authoritative business-audit model.

**RM-AUDIT-RESEARCH-0002:** Windows Event Log/ETW, Linux journald/audit/syslog, macOS Unified Logging/audit facilities, and cloud-provider audit feeds have different capture, privacy, persistence, sequencing, integrity, and access semantics; platform/provider profiles disclose exact claims.
