# Havenplanner

Planner die schepen toewijst aan ligplaatsen in de Rotterdamse haven.
Schepen worden op volgorde van aankomst ingepland op de kleinste ligplaats waar ze passen (lengte en diepgang) en die op dat moment vrij is.

## Gebruik

Vereist Python 3.10+. Geen externe dependencies.

```bash
python -m havenplanner                                  # voorbeelddata uit data/
python -m havenplanner schepen.csv ligplaatsen.csv      # eigen data
python -m unittest                                      # tests
```

## Structuur

| Pad | Inhoud |
|---|---|
| `havenplanner/modellen.py` | `Schip`, `Ligplaats`, `Toewijzing` |
| `havenplanner/planner.py` | Planningslogica |
| `havenplanner/inlezen.py` | CSV inlezen |
| `havenplanner/__main__.py` | Command-line interface |
| `data/` | Voorbeelddata |
| `tests/` | Unit tests en regressietests |
