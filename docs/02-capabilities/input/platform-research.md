# Input platform research

**Status:** Research evidence; normative conclusions live in contracts and ADRs.

## Windows

Win32 distinguishes traditional window messages from Raw Input. Traditional keyboard processing separates keystroke messages from translated character messages; Raw Input requires explicit registration, can distinguish devices, and may deliver foreground or authorized background input. High-frequency raw input can be drained in batches. Text Services Framework/IME paths manage compositions, candidates, surrounding context, and committed characters independently of raw keys.

Primary sources: [Raw Input overview](https://learn.microsoft.com/en-us/windows/win32/inputdev/about-raw-input), [`WM_INPUT`](https://learn.microsoft.com/en-us/windows/win32/inputdev/wm-input), [keyboard input](https://learn.microsoft.com/en-us/windows/win32/inputdev/keyboard-input), [Text Services Framework](https://learn.microsoft.com/en-us/windows/win32/tsf/text-services-framework), [IME composition and candidate windows](https://learn.microsoft.com/en-us/windows/win32/intl/status--composition--and-candidates-windows).

## Linux: Wayland and XKB

Wayland routes keyboard, pointer, and touch through seats and focused surfaces. Pointer coordinates are surface-local; axis events preserve source/discrete/value/stop semantics. Keyboard keymaps and modifier state are delivered separately. Relative pointer, pointer constraints, virtual keyboard/pointer, and text-input are separate protocols, confirming that focused observation, raw-relative motion, capture, injection, and composition are independent capabilities. XKB supplies physical keycode-to-symbol/modifier/group interpretation rather than text composition as one undifferentiated event.

Primary sources: [Wayland core `wl_seat` protocols](https://wayland.app/protocols/wayland#wl_seat), [text-input v3](https://wayland.app/protocols/text-input-unstable-v3), [relative pointer](https://wayland.app/protocols/relative-pointer-unstable-v1), [pointer constraints](https://wayland.app/protocols/pointer-constraints-unstable-v1), [XKB specification](https://xkbcommon.org/doc/current/keymap-text-format-v1-v2.html).

## macOS

AppKit exposes key and pointer observations through `NSEvent`, while custom text views participate in the text input manager through `NSTextInputClient`. Marked text, committed insertion, selection/surrounding ranges, and character geometry are separate protocol operations. This supports a document-revision-bound composition service rather than key-to-character synthesis.

Primary sources: [`NSEvent`](https://developer.apple.com/documentation/appkit/nsevent), [`NSTextInputClient`](https://developer.apple.com/documentation/appkit/nstextinputclient), [Cocoa text architecture](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/TextEditing/TextEditing.html).

## Derived portability conclusions

| Concern | Portable rule |
|---|---|
| Physical key vs produced text | Separate streams with optional causal link |
| Native focus | Revisioned routing input, not widget focus |
| Raw/background input | Separate authority and quality |
| Relative motion/capture | Optional independent contracts |
| IME composition | Revision-bound provisional text lifecycle |
| Injection/accessibility/remote | Preserve provenance; do not infer authorization |

