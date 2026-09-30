"""CSV-bestanden inlezen."""
import csv
from datetime import datetime
from pathlib import Path

from .modellen import Schip, Ligplaats

TIJDFORMAT = "%Y-%m-%d %H:%M"


def laad_schepen(pad: str | Path) -> list[Schip]:
    with open(pad, newline="", encoding="utf-8") as f:
        return [
            Schip(
                naam=r["naam"],
                type=r["type"],
                lengte_m=float(r["lengte_m"]),
                diepgang_m=float(r["diepgang_m"]),
                aankomst=datetime.strptime(r["aankomst"], TIJDFORMAT),
                vertrek=datetime.strptime(r["vertrek"], TIJDFORMAT),
            )
            for r in csv.DictReader(f)
        ]


def laad_ligplaatsen(pad: str | Path) -> list[Ligplaats]:
    with open(pad, newline="", encoding="utf-8") as f:
        return [
            Ligplaats(
                code=r["code"],
                terminal=r["terminal"],
                lengte_m=float(r["lengte_m"]),
                max_diepgang_m=float(r["max_diepgang_m"]),
            )
            for r in csv.DictReader(f)
        ]
