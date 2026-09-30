"""Regressietest: planning voor de voorbeelddata, zoals vastgesteld door de havenmeester."""
import unittest
from pathlib import Path

from havenplanner.inlezen import laad_schepen, laad_ligplaatsen
from havenplanner.planner import plan

DATA = Path(__file__).resolve().parents[2] / "data"

VERWACHT = {
    "Maas Voyager": "AMZ-1",
    "Nordic Hopper": "WAA-4",
    "Spido Star": "CRU-1",
    "Ever Rotterdam": "AMZ-2",
    "Waal Trader": "WAA-3",
    "Delta Tanker": "EUR-1",
    "Kinderdijk": "WAA-4",
    "Aurora Seas": "CRU-1",
    "Lekstroom": "WAA-3",
    "Hollandia": "EUR-1",
}


class TestGolden(unittest.TestCase):
    def test_planning_voorbeelddata(self):
        planning, niet = plan(laad_schepen(DATA / "schepen.csv"),
                              laad_ligplaatsen(DATA / "ligplaatsen.csv"))
        self.assertEqual({t.schip.naam: t.ligplaats.code for t in planning}, VERWACHT)
        self.assertEqual(niet, [])


if __name__ == "__main__":
    unittest.main()
