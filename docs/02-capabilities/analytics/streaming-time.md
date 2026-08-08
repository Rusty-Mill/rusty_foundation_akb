# Streaming time, watermarks, and late data

**RM-ANALYTICS-TIME-0001:** Event, ingestion, processing, and observation time are distinct tagged domains; event timestamps bind source field/extraction, unit, zone/calendar, validation, correction, and provenance.

**RM-ANALYTICS-TIME-0002:** A watermark binds stream/source partitions, watermark strategy/configuration generation, observed input frontiers, idle/finished partition policy, alignment, emission time, and monotonic event-time frontier.

**RM-ANALYTICS-TIME-0003:** A watermark asserts progress under its source/strategy assumptions and authorizes bounded state/timer decisions; it does not prove no earlier event exists, source completeness, wall-clock recency, or downstream effect.

**RM-ANALYTICS-TIME-0004:** Multiple-input watermarks declare minimum/maximum/aligned/custom combination, idle detection, skew, partition discovery/recovery, and consequences for correctness, latency, and state.

**RM-ANALYTICS-STREAM-WINDOW-0001:** Streaming tumbling/sliding/session/global/custom windows bind time domain, size/slide/gap, offset/zone/DST, keys, trigger, accumulation/retraction mode, allowed lateness, cleanup, and output identity.

**RM-ANALYTICS-LATE-0001:** Late events are accepted/update/retract, side-output/quarantined, recomputed, or dropped under explicit thresholds and audit/metrics; late relative to a watermark is not invalid data.

**RM-ANALYTICS-LATE-0002:** Corrections/retractions/upserts carry stable result keys and revisions so downstream consumers can reconcile; append-only sinks cannot silently represent revisable results.

**RM-ANALYTICS-TIME-0005:** Timers bind key/window/state generation and time domain; recovery, duplicate firing, cancellation, clock changes, and rescaling behavior are explicit.
