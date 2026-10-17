"""Regression gates for money, coverage and non-double-counting."""
import unittest
from decimal import Decimal as D
from build_procurement import NOT_IN_CAD, make_components, make_parts, make_orders, pack_count, validate


class ProcurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parts=make_parts()
        cls.orders=make_orders(cls.parts)
        cls.byid={o['id']:o for o in cls.orders}
        cls.components=make_components(cls.parts)

    def test_complete_cad_coverage_and_cost_owners(self):
        validate(self.parts,self.orders)
        self.assertEqual(sum(int(p['cad_quantity']) for p in self.parts if p['cad_quantity']),1066)

    def test_pack_rounding_does_not_underbuy(self):
        self.assertEqual(pack_count(17,4),5)
        self.assertEqual(pack_count(D('3.84'),1),4)
        self.assertEqual(pack_count(D('2.24'),1),3)
        self.assertIsNone(pack_count(None,10))

    def test_tmc_is_four_packs_not_sixteen_packs(self):
        row=self.byid['BUY-002']
        self.assertEqual(row['order_packs'],4)
        self.assertEqual(row['gross_eur'],D('159.80'))

    def test_net_price_and_fractional_units(self):
        self.assertEqual(self.byid['BUY-008']['net_eur'],D('90.24'))
        self.assertEqual(self.byid['BUY-008']['gross_eur'],D('107.39'))
        self.assertEqual(self.byid['MAT-003']['gross_eur'],D('35.00'))

    def test_unknown_prices_remain_unknown(self):
        for key in ['OPEN-CAD-075','OPEN-SYS-003','OPEN-CAD-055']:
            self.assertIsNone(self.byid[key]['gross_eur'])
            self.assertIsNone(self.byid[key]['net_eur'])

    def test_alternatives_do_not_own_original_cost(self):
        for key in ['ALT-001','ALT-002','OPT-001']:
            self.assertTrue(self.byid[key]['optional'])
            self.assertNotIn(key,{p['cost_id'] for p in self.parts})

    def test_motor_hypothesis_preserves_raw_counts(self):
        p=next(p for p in self.parts if p['id']=='CAD-063')
        self.assertEqual(int(p['cad_quantity']),8)
        self.assertEqual(p['quantity'],4)
        p=next(p for p in self.parts if p['id']=='CAD-064')
        self.assertEqual(int(p['fusion_quantity']),0)
        self.assertEqual(p['quantity'],12)

    def test_raw_material_not_costed_again_per_print(self):
        printed=[p for p in self.parts if p['group']=='3D-Druck intern']
        self.assertTrue(printed)
        self.assertEqual({p['cost_id'] for p in printed},{'MAT-001'})
        self.assertEqual(self.byid['MAT-001']['order_packs'],4)

    def test_components_cover_every_cad_part_once(self):
        validate(self.parts,self.orders,self.components)
        names={r['component'] for r in self.components}
        self.assertEqual(len(names),14)
        self.assertIn(NOT_IN_CAD,names)

    def test_missing_fusion_motors_stay_with_their_component(self):
        rows=[r for r in self.components if r['id']=='CAD-064']
        self.assertEqual(sum(r['quantity'] for r in rows),12)
        self.assertEqual({r['component'] for r in rows if r['subassembly']=='x_belt_drive'},{'K01 base:1'})
        self.assertTrue(all(r['in_fusion']=='fehlt im Fusion-Import' for r in rows))

if __name__=='__main__': unittest.main()
