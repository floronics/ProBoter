"""Extract named occurrences from the PROBoter AP214 STEP assembly.

This is a mechanical inventory, not a purchase-ready BOM. STEP product names
do not provide materials, tolerances, suppliers, or all non-CAD accessories.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


OCCURRENCE = re.compile(
    r"#\d+=NEXT_ASSEMBLY_USAGE_OCCURRENCE\((.*?)\);", re.DOTALL
)
QUOTED_NAME = re.compile(r"\s*'((?:''|[^'])*)'")
REFERENCE = re.compile(r"#(\d+)")


def _occurrence_graph(step_file: Path):
    # The upstream exporter declares raw byte strings rather than STEP escapes.
    content = step_file.read_text(encoding="latin-1")
    occurrences: list[tuple[str, str, str]] = []
    for match in OCCURRENCE.finditer(content):
        arguments = match.group(1)
        name_match = QUOTED_NAME.match(arguments)
        references = REFERENCE.findall(arguments)
        if name_match is None or len(references) != 2:
            raise ValueError(f"Cannot parse assembly occurrence at byte {match.start()}")
        name = name_match.group(1).replace("''", "'")
        occurrences.append((name, references[0], references[1]))

    if not occurrences:
        raise ValueError("No NEXT_ASSEMBLY_USAGE_OCCURRENCE entities found")

    parents = {parent for _, parent, _ in occurrences}
    children = {child for _, _, child in occurrences}
    roots = parents - children
    if len(roots) != 1:
        raise ValueError(f"Expected one assembly root, found {len(roots)}")
    graph: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for name, parent, child in occurrences:
        graph[parent].append((name, child))
    return graph, parents, next(iter(roots)), len(occurrences)


def inventory(step_file: Path) -> tuple[Counter[str], Counter[str], int, int]:
    graph, parents, root, occurrence_count = _occurrence_graph(step_file)

    # A STEP assembly definition can be placed multiple times. Expand each
    # placement from the root; counting definition edges alone undercounts it.
    cache: dict[str, tuple[Counter[str], Counter[str]]] = {}
    active: set[str] = set()

    def expand(node: str) -> tuple[Counter[str], Counter[str]]:
        if node in active:
            raise ValueError(f"Cycle in assembly definitions at #{node}")
        if node in cache:
            return cache[node]
        active.add(node)
        leaves: Counter[str] = Counter()
        assemblies: Counter[str] = Counter()
        for name, child in graph[node]:
            if child in parents:
                assemblies[name] += 1
                child_leaves, child_assemblies = expand(child)
                leaves.update(child_leaves)
                assemblies.update(child_assemblies)
            else:
                leaves[name] += 1
        active.remove(node)
        cache[node] = leaves, assemblies
        return leaves, assemblies

    leaves, assemblies = expand(root)
    if set(cache) != parents:
        raise ValueError("Assembly definitions are disconnected from the root")
    return leaves, assemblies, occurrence_count, 1


def components(step_file: Path) -> list[tuple[str, Counter[tuple[str, str]]]]:
    """Leaf counts per top-level placement, keyed by (direct subassembly, leaf).

    Parts deeper in a subassembly stay with the top-level component; the
    subassembly is the direct child of that component ('' = placed directly).
    """
    graph, parents, root, _ = _occurrence_graph(step_file)

    def leaves(node: str) -> Counter[str]:
        result: Counter[str] = Counter()
        for name, child in graph[node]:
            result.update(leaves(child) if child in parents else {name: 1})
        return result

    placements = []
    for top, node in graph[root]:
        counts: Counter[tuple[str, str]] = Counter()
        if node not in parents:
            counts[("", top)] += 1
        for name, child in graph[node] if node in parents else []:
            if child in parents:
                for leaf, quantity in leaves(child).items():
                    counts[(name, leaf)] += quantity
            else:
                counts[("", name)] += 1
        placements.append((top, counts))
    return placements


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step_file", type=Path)
    parser.add_argument("--output", type=Path, help="CSV path; stdout if omitted")
    parser.add_argument("--components", type=Path,
                        help="also write leaf counts per top-level component to this CSV")
    args = parser.parse_args()

    if args.components:
        args.components.parent.mkdir(parents=True, exist_ok=True)
        with args.components.open("w", newline="", encoding="utf-8-sig") as stream:
            writer = csv.writer(stream)
            writer.writerow(("component_index", "component", "subassembly", "cad_name", "quantity"))
            for index, (top, counts) in enumerate(components(args.step_file), 1):
                for (subassembly, name), quantity in sorted(counts.items()):
                    writer.writerow((index, top, subassembly, name, quantity))

    leaves, assemblies, occurrence_count, root_count = inventory(args.step_file)
    if root_count != 1:
        raise ValueError(f"Expected one assembly root, found {root_count}")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        stream = args.output.open("w", newline="", encoding="utf-8-sig")
    else:
        stream = sys.stdout

    try:
        writer = csv.writer(stream)
        writer.writerow(("cad_name", "quantity", "kind"))
        for name, quantity in sorted(leaves.items()):
            writer.writerow((name, quantity, "leaf"))
        for name, quantity in sorted(assemblies.items()):
            writer.writerow((name, quantity, "assembly_not_additional_purchase"))
    finally:
        if args.output:
            stream.close()

    print(
        f"{occurrence_count} definition relationships; {sum(leaves.values())} expanded leaf occurrences "
        f"across {len(leaves)} names; {sum(assemblies.values())} subassemblies "
        f"across {len(assemblies)} names",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
