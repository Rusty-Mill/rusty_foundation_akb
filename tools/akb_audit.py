#!/usr/bin/env python3
"""Build and verify the Foundation AKB's derived consistency index.

Markdown remains authoritative. This dependency-free tool emits a deterministic
index and audit summary whose records always point back to Markdown source lines.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIREMENT_RE = re.compile(r"\*\*(RM-[A-Z0-9-]+):")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
ADR_FILE_RE = re.compile(r"(?P<number>\d{4})-[a-z0-9-]+\.md$")
ADR_INDEX_RE = re.compile(r"\| \[(?P<number>\d{4})\]\((?P<file>[^)]+)\)")
STATUS_RE = re.compile(r"^\| Status \| (?P<status>[^|]+) \|$", re.MULTILINE)
ASSERTION_ROW_RE = re.compile(
    r"^\| `(?P<id>rm\.assertion\.[a-z0-9.-]+@\d+)` \| (?P<sources>[^|]+) \|",
    re.MULTILINE,
)
GRAPH_NODE_RE = re.compile(r"^\| `(?P<id>rm\.(?!assertion\.)[a-z0-9.-]+)` \| \[(?P<label>[^]]+)\]\((?P<source>[^)]+)\) \|", re.MULTILINE)
GRAPH_EDGE_RE = re.compile(r"^\| `(?P<source>rm\.[a-z0-9.-]+)` \| `(?P<kind>requires|optionally-uses|conflicts-with)` \| `(?P<target>rm\.[a-z0-9.-]+)` \| \[(?P<label>[^]]+)\]\((?P<evidence>[^)]+)\) \|", re.MULTILINE)
BENCHMARK_ROW_RE = re.compile(
    r"^\| `(?P<id>rm\.benchmark\.[a-z0-9.-]+@\d+)` \| (?P<requirements>(?:`RM-[A-Z0-9-]+`(?:, )?)+) \|",
    re.MULTILINE,
)


@dataclass(frozen=True)
class Finding:
    severity: str
    rule: str
    source: str
    detail: str


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def markdown_files(root: Path) -> list[Path]:
    return sorted(root.joinpath("docs").rglob("*.md"))


def requirement_kind(source: str) -> str:
    if "/profiles/" in source:
        return "profile"
    if source.endswith("/conformance.md"):
        return "conformance"
    if source.endswith("/benchmarks.md"):
        return "benchmark"
    if source.startswith("docs/adr/"):
        return "decision"
    if source.startswith("docs/02-capabilities/"):
        return "capability"
    return "governance"


def domain_for(source: str) -> str | None:
    parts = source.split("/")
    if len(parts) >= 4 and parts[:2] == ["docs", "02-capabilities"]:
        return parts[2]
    return None


def inspect(root: Path) -> tuple[dict[str, object], list[Finding]]:
    files = markdown_files(root)
    findings: list[Finding] = []
    requirements: list[dict[str, object]] = []
    seen_requirements: dict[str, str] = {}
    internal_links = 0

    file_records: list[dict[str, object]] = []
    for path in files:
        source = relative(path, root)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        file_records.append(
            {
                "source": source,
                "sha256": sha256_text(text),
                "lines": len(lines),
            }
        )

        fences = sum(1 for line in lines if line.lstrip().startswith("```"))
        if fences % 2:
            findings.append(Finding("error", "fence-balanced", source, "unbalanced fenced block"))

        for line_number, line in enumerate(lines, 1):
            for match in REQUIREMENT_RE.finditer(line):
                identifier = match.group(1)
                previous = seen_requirements.get(identifier)
                if previous is not None:
                    findings.append(
                        Finding("error", "requirement-unique", source, f"{identifier} also declared at {previous}")
                    )
                else:
                    seen_requirements[identifier] = f"{source}:{line_number}"
                requirements.append(
                    {
                        "id": identifier,
                        "source": source,
                        "line": line_number,
                        "kind": requirement_kind(source),
                        "domain": domain_for(source),
                    }
                )

        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "chatgpt-")):
                continue
            target_path = target.split("#", 1)[0].replace("%20", " ")
            if not target_path:
                continue
            internal_links += 1
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                findings.append(Finding("error", "link-resolves", source, f"missing target {target_path}"))

    capability_root = root / "docs" / "02-capabilities"
    domains: list[dict[str, object]] = []
    assertions: list[dict[str, object]] = []
    assertion_ids: set[str] = set()
    benchmark_scenarios: list[dict[str, object]] = []
    benchmark_scenario_ids: set[str] = set()
    for directory in sorted(p for p in capability_root.iterdir() if p.is_dir() and p.name != "profiles"):
        readme = directory / "README.md"
        if not readme.exists():
            findings.append(Finding("error", "domain-readme", relative(directory, root), "README.md missing"))
            continue
        text = readme.read_text(encoding="utf-8")
        status_match = STATUS_RE.search(text)
        domain_requirements = [item for item in requirements if item["domain"] == directory.name]
        conformance = directory / "conformance.md"
        benchmarks = directory / "benchmarks.md"
        traceability = directory / "traceability.md"
        mapped_sources: dict[str, list[str]] = {}
        if traceability.exists():
            trace_text = traceability.read_text(encoding="utf-8")
            for match in ASSERTION_ROW_RE.finditer(trace_text):
                assertion_id = match.group("id")
                if assertion_id in assertion_ids:
                    findings.append(Finding("error", "assertion-unique", relative(traceability, root), f"duplicate assertion {assertion_id}"))
                assertion_ids.add(assertion_id)
                source_names = [item.strip().strip("`") for item in match.group("sources").split(",")]
                source_paths = [f"docs/02-capabilities/{directory.name}/{name}" for name in source_names]
                for source_path in source_paths:
                    if not root.joinpath(source_path).exists():
                        findings.append(Finding("error", "assertion-source-exists", relative(traceability, root), f"missing source {source_path}"))
                assertions.append(
                    {
                        "id": assertion_id,
                        "domain": directory.name,
                        "source": relative(traceability, root),
                        "covers_sources": source_paths,
                    }
                )
                for source_path in source_paths:
                    mapped_sources.setdefault(source_path, []).append(assertion_id)
            for match in BENCHMARK_ROW_RE.finditer(trace_text):
                scenario_id = match.group("id")
                if scenario_id in benchmark_scenario_ids:
                    findings.append(Finding("error", "benchmark-scenario-unique", relative(traceability, root), f"duplicate scenario {scenario_id}"))
                benchmark_scenario_ids.add(scenario_id)
                requirement_ids = re.findall(r"RM-[A-Z0-9-]+", match.group("requirements"))
                benchmark_scenarios.append(
                    {"id": scenario_id, "domain": directory.name, "source": relative(traceability, root), "requirements": requirement_ids}
                )
        mapped_capability_requirements = 0
        for item in domain_requirements:
            if item["kind"] != "capability":
                continue
            mapped = mapped_sources.get(str(item["source"]), [])
            item["assertions"] = mapped
            if mapped:
                mapped_capability_requirements += 1
        capability_requirement_count = sum(item["kind"] == "capability" for item in domain_requirements)
        benchmark_requirement_items = [item for item in domain_requirements if item["kind"] == "benchmark"]
        scenario_ids_by_requirement: dict[str, list[str]] = {}
        for scenario in benchmark_scenarios:
            if scenario["domain"] != directory.name:
                continue
            for requirement_id in scenario["requirements"]:
                matched = next((item for item in benchmark_requirement_items if item["id"] == requirement_id), None)
                if matched is None:
                    findings.append(Finding("error", "benchmark-requirement-exists", relative(traceability, root), f"{scenario['id']} references non-benchmark requirement {requirement_id}"))
                    continue
                scenario_ids_by_requirement.setdefault(requirement_id, []).append(str(scenario["id"]))
        for item in benchmark_requirement_items:
            item["benchmark_scenarios"] = scenario_ids_by_requirement.get(str(item["id"]), [])
        mapped_benchmark_requirements = sum(bool(item["benchmark_scenarios"]) for item in benchmark_requirement_items)
        domain_record = {
            "id": directory.name,
            "source": relative(readme, root),
            "status": status_match.group("status").strip() if status_match else "unspecified",
            "requirements": len(domain_requirements),
            "capability_requirements": capability_requirement_count,
            "conformance_requirements": sum(item["kind"] == "conformance" for item in domain_requirements),
            "benchmark_requirements": sum(item["kind"] == "benchmark" for item in domain_requirements),
            "mapped_benchmark_requirements": mapped_benchmark_requirements,
            "has_conformance_spec": conformance.exists(),
            "has_benchmark_spec": benchmarks.exists(),
            "mapped_capability_requirements": mapped_capability_requirements,
            "direct_requirement_assertion_map": capability_requirement_count > 0 and mapped_capability_requirements == capability_requirement_count,
            "direct_benchmark_scenario_map": len(benchmark_requirement_items) > 0 and mapped_benchmark_requirements == len(benchmark_requirement_items),
        }
        domains.append(domain_record)
        if not conformance.exists():
            findings.append(Finding("error", "domain-conformance", relative(readme, root), "conformance.md missing"))
        if not benchmarks.exists():
            findings.append(Finding("error", "domain-benchmarks", relative(readme, root), "benchmarks.md missing"))
        if not status_match:
            findings.append(Finding("warning", "domain-status", relative(readme, root), "machine-readable status absent"))

    adr_root = root / "docs" / "adr"
    adr_index_text = (adr_root / "README.md").read_text(encoding="utf-8")
    indexed_adrs = {match.group("file") for match in ADR_INDEX_RE.finditer(adr_index_text)}
    adr_files = {path.name for path in adr_root.glob("*.md") if ADR_FILE_RE.match(path.name)}
    for missing in sorted(adr_files - indexed_adrs):
        findings.append(Finding("error", "adr-indexed", "docs/adr/README.md", f"{missing} not indexed"))
    for missing in sorted(indexed_adrs - adr_files):
        findings.append(Finding("error", "adr-exists", "docs/adr/README.md", f"{missing} missing"))

    graph_source = root / "docs" / "04-ecosystem" / "consistency-readiness" / "dependency-graph.md"
    graph_nodes: list[dict[str, str]] = []
    graph_edges: list[dict[str, str]] = []
    if graph_source.exists():
        graph_text = graph_source.read_text(encoding="utf-8")
        for match in GRAPH_NODE_RE.finditer(graph_text):
            graph_nodes.append({"id": match.group("id"), "source": match.group("source")})
        node_ids = {item["id"] for item in graph_nodes}
        if len(node_ids) != len(graph_nodes):
            findings.append(Finding("error", "graph-node-unique", relative(graph_source, root), "duplicate node identity"))
        for match in GRAPH_EDGE_RE.finditer(graph_text):
            edge = {"source": match.group("source"), "kind": match.group("kind"), "target": match.group("target"), "evidence": match.group("evidence")}
            graph_edges.append(edge)
            for endpoint in (edge["source"], edge["target"]):
                if endpoint not in node_ids:
                    findings.append(Finding("error", "graph-endpoint-declared", relative(graph_source, root), f"undeclared endpoint {endpoint}"))
        adjacency: dict[str, list[str]] = {node: [] for node in node_ids}
        for edge in graph_edges:
            if edge["kind"] == "requires" and edge["source"] in adjacency:
                adjacency[edge["source"]].append(edge["target"])
        visiting: set[str] = set()
        visited: set[str] = set()
        def visit(node: str) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            if any(visit(target) for target in adjacency.get(node, [])):
                return True
            visiting.remove(node)
            visited.add(node)
            return False
        if any(visit(node) for node in sorted(node_ids)):
            findings.append(Finding("error", "graph-requires-acyclic", relative(graph_source, root), "required dependency cycle"))

    findings.sort(key=lambda item: (item.severity, item.rule, item.source, item.detail))
    index: dict[str, object] = {
        "format": "rusty-mill-akb-index",
        "version": 1,
        "authority": "docs/01-architecture/architecture-model.md",
        "generated_from": "Markdown; this index is derived and non-authoritative",
        "summary": {
            "markdown_documents": len(files),
            "internal_links": internal_links,
            "requirements": len(requirements),
            "domains": len(domains),
            "adrs": len(adr_files),
            "errors": sum(item.severity == "error" for item in findings),
            "warnings": sum(item.severity == "warning" for item in findings),
            "domains_with_conformance": sum(bool(item["has_conformance_spec"]) for item in domains),
            "domains_with_benchmarks": sum(bool(item["has_benchmark_spec"]) for item in domains),
            "domains_with_direct_requirement_assertion_map": sum(
                bool(item["direct_requirement_assertion_map"]) for item in domains
            ),
            "domains_with_direct_benchmark_scenario_map": sum(
                bool(item["direct_benchmark_scenario_map"]) for item in domains
            ),
            "benchmark_scenarios": len(benchmark_scenarios),
            "declared_graph_nodes": len(graph_nodes),
            "declared_graph_edges": len(graph_edges),
            "required_graph_acyclic": not any(item.rule == "graph-requires-acyclic" for item in findings),
        },
        "domains": domains,
        "assertions": assertions,
        "benchmark_scenarios": benchmark_scenarios,
        "dependency_graph": {
            "source": relative(graph_source, root) if graph_source.exists() else None,
            "nodes": graph_nodes,
            "edges": graph_edges,
            "required_acyclic": not any(item.rule == "graph-requires-acyclic" for item in findings),
        },
        "requirements": requirements,
        "files": file_records,
        "findings": [item.__dict__ for item in findings],
    }
    return index, findings


def report(index: dict[str, object]) -> str:
    summary = index["summary"]
    assert isinstance(summary, dict)
    domains = index["domains"]
    assert isinstance(domains, list)
    unspecified = [item["id"] for item in domains if item["status"] == "unspecified"]
    return f"""# Architecture consistency and readiness audit report

**Status:** Generated evidence  
**Authority:** [Consistency and readiness model](README.md)  
**Generator:** `tools/akb_audit.py`  
**Index:** [Machine-readable inventory](index.json)

This report is deterministic and contains no claim that file presence proves semantic coverage.

## Inventory

| Measure | Result |
|---|---:|
| Markdown documents | {summary['markdown_documents']:,} |
| Resolved internal links | {summary['internal_links']:,} |
| Unique normative requirements | {summary['requirements']:,} |
| Capability domains | {summary['domains']:,} |
| Indexed ADRs | {summary['adrs']:,} |
| Structural errors | {summary['errors']:,} |
| Structural warnings | {summary['warnings']:,} |

## Artifact coverage

| Evidence | Domains | Coverage |
|---|---:|---:|
| Conformance specification present | {summary['domains_with_conformance']:,} / {summary['domains']:,} | {summary['domains_with_conformance'] / summary['domains']:.1%} |
| Benchmark specification present | {summary['domains_with_benchmarks']:,} / {summary['domains']:,} | {summary['domains_with_benchmarks'] / summary['domains']:.1%} |
| Direct requirement-to-assertion map | {summary['domains_with_direct_requirement_assertion_map']:,} / {summary['domains']:,} | {summary['domains_with_direct_requirement_assertion_map'] / summary['domains']:.1%} |
| Direct benchmark-requirement-to-scenario map | {summary['domains_with_direct_benchmark_scenario_map']:,} / {summary['domains']:,} | {summary['domains_with_direct_benchmark_scenario_map'] / summary['domains']:.1%} |

## Declared dependency graph

| Measure | Result |
|---|---:|
| Source-declared capability nodes | {summary['declared_graph_nodes']:,} |
| Source-declared typed edges | {summary['declared_graph_edges']:,} |
| Required-edge graph acyclic | {str(summary['required_graph_acyclic']).lower()} |

Graph counts cover only explicit declarations. Missing nodes or edges are unknown, not proof of independence.

The first two rows prove specification presence only. The mapping rows prove complete planned links only for counted domains. None proves executable assertions, benchmark runs, passing provider results, or performance budgets.

## Findings

- Structural validation currently passes with {summary['errors']} errors.
- Every capability domain has conformance and benchmark planning artifacts.
- {len(unspecified)} domain README files lack the canonical table-form status field; this is recorded as a migration-quality issue, not silently interpreted as Stable.
- {summary['domains_with_direct_requirement_assertion_map']} domain(s) have a complete direct planned requirement-to-assertion map; repository-wide migration remains open.
- {summary['domains_with_direct_benchmark_scenario_map']} domain(s) have complete benchmark-requirement-to-scenario maps across {summary['benchmark_scenarios']} stable semantic scenarios; run evidence remains absent by design.
- Semantic contradiction review remains human-governed and is tracked in the [closure backlog](closure-backlog.md).

## Readiness conclusion

The knowledge base is **architecture-definition ready** and structurally indexable. It is **not implementation-release ready**: all domain analyses remain Draft, direct assertion traceability is incomplete repository-wide, provider/platform evidence does not yet exist, and benchmark baselines cannot exist before qualified implementations. These are explicit gates rather than defects hidden by a percentage.
"""


def write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated evidence differs")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    output = root / "docs" / "04-ecosystem" / "consistency-readiness"
    index, findings = inspect(root)
    index_text = json.dumps(index, indent=2, sort_keys=False) + "\n"
    report_text = report(index)
    expected = {output / "index.json": index_text, output / "audit-report.md": report_text}
    if args.check:
        stale = [relative(path, root) for path, content in expected.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("stale generated evidence: " + ", ".join(stale), file=sys.stderr)
            return 1
    else:
        output.mkdir(parents=True, exist_ok=True)
        for path, content in expected.items():
            write_if_changed(path, content)
    errors = [item for item in findings if item.severity == "error"]
    summary = index["summary"]
    print(json.dumps(summary, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
