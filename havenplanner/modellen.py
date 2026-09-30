"""Domeinmodellen voor de havenplanner."""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Schip:
    naam: str
    type: str            # 'container', 'bulk', 'tanker' of 'cruise'
    lengte_m: float
    diepgang_m: float
    aankomst: datetime
    vertrek: datetime

    def __post_init__(self):
        if self.vertrek <= self.aankomst:
            raise ValueError(f"{self.naam}: vertrek moet na aankomst liggen")


@dataclass(frozen=True)
class Ligplaats:
    code: str
    terminal: str
    lengte_m: float
    max_diepgang_m: float

    def past(self, schip: Schip) -> bool:
        """Past het schip fysiek aan deze ligplaats?"""
        return schip.lengte_m <= self.lengte_m and schip.diepgang_m <= self.max_diepgang_m


@dataclass(frozen=True)
class Toewijzing:
    schip: Schip
    ligplaats: Ligplaats
