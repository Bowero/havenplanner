"""Gebruik: python -m havenplanner [schepen.csv] [ligplaatsen.csv]"""
import sys

from .inlezen import laad_schepen, laad_ligplaatsen
from .planner import plan


def formatteer(planning, niet_geplaatst) -> str:
    regels = [f"{'SCHIP':<22}{'TYPE':<11}{'LIGPLAATS':<11}{'AANKOMST':<18}VERTREK"]
    for t in sorted(planning, key=lambda t: (t.schip.aankomst, t.schip.naam)):
        s = t.schip
        regels.append(
            f"{s.naam:<22}{s.type:<11}{t.ligplaats.code:<11}"
            f"{s.aankomst:%Y-%m-%d %H:%M}  {s.vertrek:%Y-%m-%d %H:%M}"
        )
    if niet_geplaatst:
        regels.append("")
        regels.append("NIET GEPLAATST: " + ", ".join(s.naam for s in niet_geplaatst))
    return "\n".join(regels)


def main(argv: list[str]) -> int:
    schepen_pad = argv[1] if len(argv) > 1 else "data/schepen.csv"
    ligplaatsen_pad = argv[2] if len(argv) > 2 else "data/ligplaatsen.csv"
    planning, niet_geplaatst = plan(laad_schepen(schepen_pad), laad_ligplaatsen(ligplaatsen_pad))
    print(formatteer(planning, niet_geplaatst))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
