# Data-transfer cross-cutting requirements

## Security and privacy

Clipboard and drag payloads may contain credentials, shell commands, paths, rich markup, URLs, images with parser exploits, executables, or tracking data. Consumers validate by selected representation and destination context, apply size/decompression/parser bounds, keep previews inert, and require confirmation for privileged/destructive effects. Origin labels are advisory, not trust.

Password/secure fields, terminal secure-input mode, private browsing, protected documents, remote sessions, and enterprise DLP may prohibit or constrain copy/paste/drag. Degradation is visible; no provider claims content cannot be captured after transfer.

## Accessibility

Copy, cut, paste, drag source/target, allowed operation, insertion position, rejected reason, progress, cancellation, and completion are semantic actions/states/events. Pointer drag is never the sole path. Time limits, autoscroll, animation, drag imagery, and spatial target selection honor preferences and assistive workflows.

## Internationalization

Text formats declare encoding/newlines and preserve semantic Unicode. Suggested filenames use lossless filesystem semantic values after target validation; display strings and actual path values remain distinct. Format identifiers and filenames are not localized for protocol matching. Rich content carries language/direction metadata where supported.

## Observability

Events record correlation, offer/representation identifiers, byte counts, duration, conversion, operation, cancellation/failure class, and policy decision without content, filenames, URLs, target paths, application identity, or assistive-technology identity by default.

