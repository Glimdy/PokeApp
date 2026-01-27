"""
Script to fix the most critical Pokemon size errors in pokemon_extra_data.py
Fixes entries with sizes that are wildly off (like Steelix being 0.9m instead of 8.8m)
"""

critical_fixes = {
    95: {"height": 8.8, "weight": 213.0},   # Onix
    130: {"height": 6.5, "weight": 235.0},  # Gyarados
    147: {"height": 1.8, "weight": 3.3},    # Dratini
    148: {"height": 4.0, "weight": 16.5},   # Dragonair
    208: {"height": 8.8, "weight": 400.0},  # Steelix
    232: {"height": 1.1, "weight": 35.0},   # Wooper (Johto)
    246: {"height": 0.6, "weight": 35.8},   # Larvitar
    249: {"height": 5.2, "weight": 216.0},  # Lugia
    250: {"height": 3.8, "weight": 199.0},  # Ho-Oh
    330: {"height": 2.0, "weight": 68.0},   # Flygon
    334: {"height": 1.1, "weight": 20.6},   # Altaria
    371: {"height": 0.6, "weight": 21.5},   # Bagon
    372: {"height": 1.1, "weight": 110.5},  # Shelgon
    373: {"height": 1.5, "weight": 102.2},  # Salamence
    374: {"height": 0.6, "weight": 95.2},   # Beldum
    375: {"height": 1.2, "weight": 202.5},  # Metang
    376: {"height": 1.6, "weight": 550.0},  # Metagross
    384: {"height": 7.0, "weight": 206.5},  # Rayquaza
    445: {"height": 1.9, "weight": 95.0},   # Garchomp
}

# Generate replace statements
print("To fix these entries, use the following replace statements:")
print("=" * 80)

from pokemon_extra_data import POKEMON_EXTRA_DATA

replacements = []
for pokemon_id, new_data in critical_fixes.items():
    current = POKEMON_EXTRA_DATA[pokemon_id]
    color = current.get('color', 'unknown')
    replacement = f'    {pokemon_id}: {{"height": {new_data["height"]}, "weight": {new_data["weight"]}, "color": "{color}"}}'
    replacements.append(replacement)
    
print(f"# Critical Pokemon size fixes - {len(replacements)} entries to update")
for r in replacements:
    print(r + ",")
