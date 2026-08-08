# Camera and media-capture platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | Media Foundation capture sources/Source Reader and media types; Windows camera privacy policy; device controls and frame metadata vary by driver | Device activation and data flow are separate from enumeration; negotiated media types and Source Reader transformations must be disclosed; permission/policy can change |
| Linux | V4L2 formats/controls/streaming queues/timestamp flags; media-controller topology; PipeWire camera graph and desktop portal policy in sandboxed sessions | Buffer methods, planes, controls, timestamp sources, and media topology are explicit; direct `/dev/video*` and session-mediated PipeWire/portal access are different provider/authority qualities |
| macOS | AVFoundation authorization, capture devices/inputs/sessions/connections/outputs, sample buffers and session clocks | Authorization precedes session start; session graph can contain multiple inputs/outputs; sample delivery queues and retained buffers directly affect drops |

## Primary sources

- Microsoft, [Audio/video capture in Media Foundation](https://learn.microsoft.com/windows/win32/medfound/audio-video-capture-in-media-foundation), [Capture device enumeration](https://learn.microsoft.com/windows/win32/medfound/audio-video-capture-in-media-foundation#enumerate-capture-devices), and [Source Reader](https://learn.microsoft.com/windows/win32/medfound/source-reader)
- Linux kernel, [V4L2 userspace API](https://docs.kernel.org/userspace-api/media/v4l/v4l2.html), [formats](https://docs.kernel.org/userspace-api/media/v4l/dev-formats.html), [streaming I/O](https://docs.kernel.org/userspace-api/media/v4l/io.html), [buffers/timestamps](https://docs.kernel.org/userspace-api/media/v4l/buffer.html), and [controls](https://docs.kernel.org/userspace-api/media/v4l/control.html)
- PipeWire, [Streams](https://docs.pipewire.org/page_streams.html) and [SPA video format](https://docs.pipewire.org/group__spa__param.html)
- Apple, [Setting up a capture session](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session), [requesting authorization](https://developer.apple.com/documentation/avfoundation/requesting-authorization-to-capture-and-save-media), and [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput)

## Synthesis

All targets support negotiated streaming raw frames but differ in permission mediation, graph topology, format transformation, buffers, clocks, controls, and interruption. A truthful contract preserves those dimensions and treats each session as a generation with explicit authority. Encoding and file/photo-library persistence remain downstream services.
