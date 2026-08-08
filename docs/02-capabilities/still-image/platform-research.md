# Platform research

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Codec framework | Windows Imaging Component (WIC), extensible installed codecs/metadata handlers; Windows.Graphics.Imaging for selected app paths | No universal OS codec contract; libraries, desktop services, portals, sandbox helpers, and hardware APIs vary | Image I/O (`CGImageSource`/`CGImageDestination`) with system codecs/metadata; Core Image/VideoToolbox paths vary by workload |
| Incremental/multi-frame | WIC progressive levels for supported codecs and frame/container interfaces | Provider-specific streaming/progressive/tile/frame behavior | Incremental `CGImageSource`; per-index properties/images; destination finalization |
| Metadata/color | WIC metadata readers/writers/color contexts and extensible handlers | Library/schema-specific EXIF/XMP/IPTC/ICC handling | Image I/O properties/XMP metadata and ColorSync integration |
| Acceleration/isolation | WIC/native codec path varies; hardware APIs are format/workload specific | VA-API/Vulkan/video/image paths are provider-specific; sandboxing typically application/distribution-owned | System frameworks may accelerate internally; Metal/Core Image/VideoToolbox paths expose different semantics |

## Portability findings

1. WIC separates container decoder, frame decoder, metadata handlers, transforms, discovery/arbitration, and progressive support. Its extensibility means provider provenance is security-relevant.
2. Apple Image I/O exposes opaque sources/destinations, frame indices, metadata, thumbnails, incremental update, and finalization; supported formats and properties are OS-version dependent.
3. Linux distributions do not provide one stable cross-desktop image-codec service. In-process libraries, sandboxed helpers, portals, and hardware providers must resolve by exact capability and evidence.
4. Format specifications define bitstreams, not safe resource policy, threading, platform metadata behavior, or application accessibility. Rusty Mill contracts those separately.

## Primary references

- [Microsoft: Windows Imaging Component overview](https://learn.microsoft.com/en-us/windows/win32/wic/-wic-about-windows-imaging-codec)
- [Microsoft: How WIC works](https://learn.microsoft.com/en-us/windows/win32/wic/-wic-howwicworks)
- [Microsoft: WIC progressive decoding](https://learn.microsoft.com/en-us/windows/win32/wic/-wic-progressive-decoding)
- [Apple: Image I/O](https://developer.apple.com/documentation/imageio)
- [PNG specification](https://www.w3.org/TR/png-3/)
- [AV1 Bitstream & Decoding Process Specification](https://aomediacodec.github.io/av1-spec/av1-spec.pdf)
