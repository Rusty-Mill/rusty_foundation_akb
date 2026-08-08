# Schema evolution and resolution

**RM-INTERCHANGE-EVOLVE-0001:** Compatibility is directional and names writer/reader schema generations, format/mapping, forward/backward/full/transitive scope, accepted values, unknown behavior, and semantic—not merely parse—preservation.

**RM-INTERCHANGE-EVOLVE-0002:** Changes classify add/remove/reserve/rename/retag, presence/default/cardinality, numeric widening/narrowing, enum/union variant, map/list/set, nesting, constraint, semantic reinterpretation, canonical-view, and format-specific compatibility.

**RM-INTERCHANGE-EVOLVE-0003:** Removed numeric tags, names, enum values, OIDs, and discriminants remain reserved where reuse could reinterpret stored or delayed data.

**RM-INTERCHANGE-EVOLVE-0004:** Reader/writer resolution produces an explicit plan for matches, aliases, defaults, promotions/coercions, unknown retention/drop, union selection, constraint changes, loss, and rejection.

**RM-INTERCHANGE-EVOLVE-0005:** Defaults applied during decode are distinguished from values present on the wire and from application defaults; reserialization cannot silently assert presence or erase provenance.

**RM-INTERCHANGE-EVOLVE-0006:** Mixed-version rollout covers producers, consumers, intermediaries, registries, persisted messages, caches, signatures, replay/dead-letter data, rollback, and retirement.

**RM-INTERCHANGE-EVOLVE-0007:** Compatibility checks use golden old/new schemas and values plus semantic assertions; schema-diff classification alone cannot prove application compatibility.
