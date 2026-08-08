# Platform research

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Pipeline | Media Foundation sources/transforms/sinks/session; Source Reader/Sink Writer for lower-level paths | GStreamer/PipeWire and codec libraries/hardware APIs are common but not one universal OS contract | AVFoundation assets/readers/writers/player, VideoToolbox/AudioToolbox/CoreMedia |
| Time/sync | Presentation clock and selected time source; audio renderer can source time | GStreamer clock/base-time/running-time/segment model; sinks synchronize buffers | `CMTime`/`CMTimebase`, host/device clocks, `AVPlayer` coordination |
| Seek/buffer | Media source/session seek with keyframe/preroll and sink trim/drop behavior | Segment seek, flush, preroll, buffering/latency messages vary by pipeline/source | Tolerance-bearing `AVPlayer` seeks, loaded/seekable ranges, item status |
| Hardware/protection | Media Foundation transforms, DX surfaces, protected media paths by provider | VA-API/Vulkan/vendor decode plus compositor/protected path support varies | VideoToolbox and protected playback paths under platform/content policy |

## Portability findings

1. Media Foundation explicitly distinguishes media time, sample timestamps, presentation time, presentation clock, and time source; audio hardware may provide the preferred clock.
2. GStreamer distinguishes buffer timestamps, stream/running time, base time, segments, clock selection, and sink synchronization; its model confirms that rate/seek are mappings, not scalar cursor changes.
3. Apple uses exact `CMTime`; seek APIs accept tolerances because efficient attainable positions can differ from requests. AVFoundation high-level playback and lower-level reader/writer/codec paths expose different control/evidence.
4. Platform frameworks are provider candidates. Exact codecs, containers, features, hardware/protected paths, low-latency behavior, and third-party components vary by OS version, packaging, policy, and hardware.

## Primary references

- [Microsoft: Media Foundation Presentation Clock](https://learn.microsoft.com/en-us/windows/win32/medfound/presentation-clock)
- [GStreamer: Clocks and synchronization](https://gstreamer.freedesktop.org/documentation/application-development/advanced/clocks.html)
- [GStreamer: Synchronisation design](https://gstreamer.freedesktop.org/documentation/additional/design/synchronisation.html)
- [Apple: AVFoundation](https://developer.apple.com/av-foundation/)
- [Apple: `AVPlayer.seek`](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:))
- [W3C: WebCodecs](https://www.w3.org/TR/webcodecs/)
