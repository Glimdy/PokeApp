"""
Script to apply critical Pokemon size fixes to pokemon_extra_data.py
Reads the file, applies fixes, and writes it back
"""
import re

# List of critical fixes
fixes = {
    208: {"height": 8.8, "weight": 400.0},  # Steelix
    130: {"height": 6.5, "weight": 235.0},  # Gyarados
    147: {"height": 1.8, "weight": 3.3},    # Dratini
    148: {"height": 4.0, "weight": 16.5},   # Dragonair
    232: {"height": 1.1, "weight": 35.0},   # Wooper
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

# Read the file
with open('pokemon_extra_data.py', 'r') as f:
    content = f.read()

# Apply each fix
for pokemon_id, new_values in fixes.items():
    # Find the line with this pokemon_id
    pattern = rf'{pokemon_id}: {{"height": [\d.]+, "weight": [\d.]+, "color": "([^"]+)"}}'
    
    def replace_func(match):
        color = match.group(1)
        return f'{pokemon_id}: {{"height": {new_values["height"]}, "weight": {new_values["weight"]}, "color": "{color}"}}'
    
    content = re.sub(pattern, replace_func, content)
    print(f"✓ Fixed Pokemon ID {pokemon_id}")

# Write the file back
with open('pokemon_extra_data.py', 'w') as f:
    f.write(content)

print("\n✓ All critical fixes applied!")
