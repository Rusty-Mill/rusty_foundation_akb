# SMS, MMS, RCS, and messaging-provider binding

**RM-COMMS-SMS-0001:** Binding states channel, sender type/number/service/brand/campaign, recipient E.164 endpoint, country/route, encoding, segment calculation, concatenation, media, provider/carrier profile, validity, and cost limits.

**RM-COMMS-SMS-0002:** SMS, MMS, RCS, WhatsApp-like provider channels, and voice are separate profiles with different identity, consent, template, session, encryption, delivery/read receipt, rich-content, and registration rules.

**RM-COMMS-SMS-0003:** Provider queued/sent, carrier accepted, delivery receipt, handset delivery, read receipt, reply, and domain effect remain distinct. Delivery receipts are provider/carrier claims with variable availability and timestamp quality.

**RM-COMMS-SMS-0004:** STOP/START/HELP and localized/provider-specific keywords map through explicit sender/program/jurisdiction policy, take idempotent suppression effects, generate bounded acknowledgements, and reconcile provider-managed opt-outs.

**RM-COMMS-SMS-0005:** Number verification/control evidence expires and handles reassignment, porting, shared/family phones, roaming, landlines, premium routes, unreachable states, and changed consent; possession is not durable person identity.

**RM-COMMS-SMS-0006:** Segment count, Unicode normalization/non-normalization, grapheme safety, transliteration prohibition/default, URL shortening, media fetch, and truncation are explicit; content changes create a new render generation.

**RM-COMMS-SMS-0007:** Sender/route selection observes registration, geography, throughput, reputation, quiet hours, emergency restrictions, and failover without evading recipient suppression or local rules.
