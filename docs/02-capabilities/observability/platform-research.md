# Platform and standards research

Research guides adapters without turning native facilities into portable semantics.

| Platform | Telemetry mechanisms | Crash mechanisms | Important variance |
|---|---|---|---|
| Windows | ETW providers/sessions/consumers; Event Log where appropriate | Windows Error Reporting and minidump facilities | ETW may lose events under size, buffer, consumer, or storage pressure. WER policy/consent and dump types vary. |
| Linux | systemd journal structured fields where present; syslog/perf tracing alternatives | kernel core-dump policy and systemd-coredump where present | systemd is not universal; core limits, namespaces, handlers, storage, and retention vary. Core images may expose broad process memory. |
| macOS | Unified Logging, activities/signposts, OSLogStore access under policy | OS-generated crash/diagnostic reports | Privacy rendering, persistence, entitlement/tool access, and user diagnostic-sharing policy constrain capture and retrieval. |

OpenTelemetry informs interoperable trace, metric, log, resource, and propagation mappings, but Rusty Mill's producer contract remains exporter/protocol neutral.

## Primary references

- [Microsoft: About Event Tracing](https://learn.microsoft.com/windows/win32/etw/about-event-tracing)
- [Microsoft: Windows Error Reporting](https://learn.microsoft.com/windows/win32/api/_wer/)
- [freedesktop.org: systemd journal fields](https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html)
- [freedesktop.org: systemd-coredump](https://www.freedesktop.org/software/systemd/man/latest/systemd-coredump.html)
- [Apple: Logging](https://developer.apple.com/documentation/os/logging)
- [Apple: Acquiring crash reports and diagnostic logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs)
- [OpenTelemetry specifications](https://opentelemetry.io/docs/specs/)

## Research conclusions

1. Loss disclosure is mandatory; native telemetry pipelines are not lossless.
2. Native stores have different access, retention, privacy, and schema constraints, so export quality is negotiated.
3. Fatal capture must cooperate with platform handlers and defer complex work to a separate process or later launch.
4. Exact build and symbol identities are required for reproducible crash analysis.

