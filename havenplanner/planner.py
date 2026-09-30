"""Kernlogica: schepen toewijzen aan ligplaatsen."""
from .modellen import Schip, Ligplaats, Toewijzing


def overlapt(a: Schip, b: Schip) -> bool:
    """Liggen twee schepen tegelijk in de haven?

    Een schip dat om 10:00 vertrekt en een schip dat om 10:00 aankomt,
    zitten elkaar NIET in de weg (aansluitend is toegestaan).
    """
    return a.aankomst <= b.vertrek and b.aankomst <= a.vertrek


def is_vrij(ligplaats: Ligplaats, schip: Schip, planning: list[Toewijzing]) -> bool:
    for t in planning:
        if t.ligplaats.code == ligplaats.code and overlapt(t.schip, schip):
            return False
    return True


def plan(schepen: list[Schip], ligplaatsen: list[Ligplaats]):
    """Greedy planner: schepen op volgorde van aankomst, kleinste passende ligplaats eerst.

    Geeft (planning, niet_geplaatst) terug.
    """
    planning: list[Toewijzing] = []
    niet_geplaatst: list[Schip] = []
    kandidaten = sorted(ligplaatsen, key=lambda l: (l.lengte_m, l.code))

    for schip in sorted(schepen, key=lambda s: (s.aankomst, s.naam)):
        for lp in kandidaten:
            if lp.past(schip) and is_vrij(lp, schip, planning):
                planning.append(Toewijzing(schip, lp))
                break
        else:
            niet_geplaatst.append(schip)
    return planning, niet_geplaatst
