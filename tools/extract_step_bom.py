"""Extract named occurrences from the PROBoter AP214 STEP assembly.

This is a mechanical inventory, not a purchase-ready BOM. STEP product names
do not provide materials, tolerances, suppliers, or all non-CAD accessories.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path


OCCURRENCE = re.compile(
    r"#\d+=NEXT_ASSEMBLY_USAGE_OCCURRENCE\((.*?)\);", re.DOTALL
)
QUOTED_NAME = re.compile(r"\s*'((?:''|[^'])*)'")
REFERENCE = re.compile(r"#(\d+)")


def inventory(step_file: Path) -> tuple[Counter[str], Counter[str], int, int]:
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
    leaves = Counter(name for name, _, child in occurrences if child not in parents)
    assemblies = Counter(name for name, _, child in occurrences if child in parents)
    return leaves, assemblies, len(occurrences), len(parents - children)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step_file", type=Path)
    parser.add_argument("--output", type=Path, help="CSV path; stdout if omitted")
    args = parser.parse_args()

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
        f"{occurrence_count} occurrences; {sum(leaves.values())} leaf parts "
        f"across {len(leaves)} names; {sum(assemblies.values())} subassemblies "
        f"across {len(assemblies)} names",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
