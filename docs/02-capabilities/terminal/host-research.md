# Terminal host standards and platform research

**Status:** Research input

## Control protocols

ECMA-48 defines control functions for coded character-imaging devices and explicitly permits implementations to support selected facilities. Modern terminal dialects add DEC/xterm and private extensions; therefore ECMA-48 is a baseline vocabulary, not a full compatibility profile. Windows documents a supported VT sequence set and notes that sequences may be split at any byte boundary.

Sources:

- Ecma International: [ECMA-48](https://ecma-international.org/publications-and-standards/standards/ecma-48/)
- Microsoft: [Console Virtual Terminal Sequences](https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)

## Unicode

Unicode supplies algorithms/properties for grapheme boundaries, East Asian width, and bidirectional ordering. Terminal cell layout still needs an explicit versioned policy for emoji, ambiguous width, combining/orphan behavior, and interaction with application cursor assumptions.

Sources:

- Unicode: [UAX #29 Text Segmentation](https://www.unicode.org/reports/tr29/)
- Unicode: [UAX #11 East Asian Width](https://www.unicode.org/reports/tr11/)
- Unicode: [UAX #9 Bidirectional Algorithm](https://www.unicode.org/reports/tr9/)

## Accessibility

WAI-ARIA defines platform-web mappings including ordered log/live-region concepts, but a native terminal must map the same semantic model through UI Automation, macOS Accessibility, or another host API. Rapid arbitrary screen mutation requires coalescing and navigable history rather than announcing raw updates.

Sources:

- W3C: [WAI-ARIA](https://www.w3.org/TR/wai-aria/) and [`log` live-region technique](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA23)
- Microsoft: [UI Automation overview](https://learn.microsoft.com/en-us/dotnet/framework/ui-automation/ui-automation-overview)
- Apple: [Accessibility](https://developer.apple.com/accessibility/)

## Security findings

Terminal control protocols can request clipboard, hyperlinks, titles, notifications, files/images, and host queries. These are authority-bearing effects, not mere formatting. Unbounded control strings, misleading links, bidi/control characters, escape injection in diagnostics, and recorded passwords are explicit threats.

