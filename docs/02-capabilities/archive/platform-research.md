# Format and platform research

## Format evidence

- [RFC 1950](https://www.rfc-editor.org/rfc/rfc1950), [RFC 1951](https://www.rfc-editor.org/rfc/rfc1951), and [RFC 1952](https://www.rfc-editor.org/rfc/rfc1952) distinguish zlib framing, DEFLATE compressed data, and gzip members.
- [RFC 7932](https://www.rfc-editor.org/rfc/rfc7932) specifies Brotli; [RFC 8878](https://www.rfc-editor.org/rfc/rfc8878) specifies independent Zstandard frames, checksums, dictionaries, and skippable frames.
- [XZ file format](https://tukaani.org/xz/xz-file-format.txt) specifies streams, blocks, indexes, checks, concatenation, and padding.
- [PKWARE APPNOTE](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) defines ZIP local records, central directory, ZIP64, split archives, methods, encryption records, and extensible extra fields.
- [POSIX pax](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/pax.html) defines portable archive interchange and exposes pathname, link, ownership, mode, time, and implementation-extension tensions.
- [Reproducible Builds archive metadata guidance](https://reproducible-builds.org/docs/archives/) identifies ordering, timestamps, ownership, permissions, and tool behavior as byte-reproducibility inputs.

## Platform evidence

- Windows exposes ZIP through [.NET `ZipArchive`](https://learn.microsoft.com/dotnet/api/system.io.compression.ziparchive), TAR through [`System.Formats.Tar`](https://learn.microsoft.com/dotnet/api/system.formats.tar), and libarchive-based [`tar`](https://learn.microsoft.com/windows/tar/). Their feature, buffering, metadata, update, and safety behavior differs.
- Microsoft's [ZIP and TAR safety guidance](https://learn.microsoft.com/dotnet/standard/io/zip-tar-best-practices) requires explicit expanded-size/count limits, destination containment, and link handling for untrusted archives.
- Linux commonly exposes general codecs as libraries and archive formats through tools/libraries rather than one stable kernel abstraction. Filesystem path, link, xattr, ACL, sparse, and mount behavior remains provider/filesystem-specific.
- Apple's [Compression framework](https://developer.apple.com/documentation/compression) separates buffer and streaming codecs. [Apple Archive](https://developer.apple.com/documentation/applearchive) additionally models archive attributes, streaming/random access, digests, error correction, sparse files, and encrypted archives.

## Architectural inference

No platform supplies the complete portable contract. Rusty Mill therefore standardizes capability semantics, budgets, evidence, and safe effect boundaries while providers disclose exact format and metadata coverage.
