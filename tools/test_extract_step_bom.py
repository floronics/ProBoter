"""Regression checks for shared STEP assembly definitions."""

import tempfile
import unittest
from pathlib import Path

from extract_step_bom import inventory


class AssemblyInventoryTests(unittest.TestCase):
    def inventory_from(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assembly.stp"
            path.write_text(text, encoding="latin-1")
            return inventory(path)

    def test_repeated_nested_assembly_is_counted_per_placement(self):
        leaves, assemblies, definitions, roots = self.inventory_from("""
#1=NEXT_ASSEMBLY_USAGE_OCCURRENCE('module','', '',#100,#200,$);
#2=NEXT_ASSEMBLY_USAGE_OCCURRENCE('module','', '',#100,#200,$);
#3=NEXT_ASSEMBLY_USAGE_OCCURRENCE('bracket','', '',#200,#300,$);
#4=NEXT_ASSEMBLY_USAGE_OCCURRENCE('bracket','', '',#200,#300,$);
#5=NEXT_ASSEMBLY_USAGE_OCCURRENCE('bolt','', '',#300,#400,$);
#6=NEXT_ASSEMBLY_USAGE_OCCURRENCE('bolt','', '',#300,#400,$);
#7=NEXT_ASSEMBLY_USAGE_OCCURRENCE('base','', '',#100,#500,$);
""")
        self.assertEqual(leaves, {"bolt": 8, "base": 1})
        self.assertEqual(assemblies, {"module": 2, "bracket": 4})
        self.assertEqual((definitions, roots), (7, 1))

    def test_reachable_cycle_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Cycle"):
            self.inventory_from("""
#1=NEXT_ASSEMBLY_USAGE_OCCURRENCE('module','', '',#100,#200,$);
#2=NEXT_ASSEMBLY_USAGE_OCCURRENCE('loop','', '',#200,#200,$);
""")

    def test_multiple_roots_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "one assembly root"):
            self.inventory_from("""
#1=NEXT_ASSEMBLY_USAGE_OCCURRENCE('part','', '',#100,#200,$);
#2=NEXT_ASSEMBLY_USAGE_OCCURRENCE('part','', '',#300,#200,$);
""")


if __name__ == "__main__":
    unittest.main()
