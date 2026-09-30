import unittest
from datetime import datetime

from havenplanner.modellen import Schip, Ligplaats
from havenplanner.planner import overlapt, plan


def schip(naam, aankomst, vertrek, lengte=200, diepgang=10, type_="bulk"):
    return Schip(naam, type_, lengte, diepgang,
                 datetime.fromisoformat(aankomst), datetime.fromisoformat(vertrek))


class TestOverlap(unittest.TestCase):
    def test_gelijktijdig_overlapt(self):
        a = schip("A", "2026-10-08 06:00", "2026-10-08 12:00")
        b = schip("B", "2026-10-08 10:00", "2026-10-08 14:00")
        self.assertTrue(overlapt(a, b))

    def test_los_van_elkaar_overlapt_niet(self):
        a = schip("A", "2026-10-08 06:00", "2026-10-08 08:00")
        b = schip("B", "2026-10-08 10:00", "2026-10-08 14:00")
        self.assertFalse(overlapt(a, b))

    def test_aansluitend_is_geen_overlap(self):
        a = schip("A", "2026-10-08 06:00", "2026-10-08 10:00")
        b = schip("B", "2026-10-08 10:00", "2026-10-08 14:00")
        self.assertFalse(overlapt(a, b))


class TestPlan(unittest.TestCase):
    def test_te_groot_schip_wordt_niet_geplaatst(self):
        lp = [Ligplaats("X-1", "Test", 150, 9)]
        planning, niet = plan([schip("Groot", "2026-10-08 06:00", "2026-10-08 12:00")], lp)
        self.assertEqual(planning, [])
        self.assertEqual([s.naam for s in niet], ["Groot"])

    def test_kleinste_passende_ligplaats_eerst(self):
        lp = [Ligplaats("GROOT", "Test", 400, 16), Ligplaats("KLEIN", "Test", 220, 11)]
        planning, _ = plan([schip("A", "2026-10-08 06:00", "2026-10-08 12:00")], lp)
        self.assertEqual(planning[0].ligplaats.code, "KLEIN")


if __name__ == "__main__":
    unittest.main()
