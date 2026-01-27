"""
Script to apply remaining Pokemon size fixes
"""
import re

# Remaining fixes
fixes = {
    103: {"height": 2.0, "weight": 120.0},  # Exeggutor
    110: {"height": 1.2, "weight": 9.5},    # Weezing
    131: {"height": 2.5, "weight": 220.0},  # Lapras
    149: {"height": 2.2, "weight": 210.0},  # Dragonite
    149: {"height": 2.2, "weight": 210.0},  # Dragonite
    226: {"height": 2.1, "weight": 220.0},  # Mantine
    227: {"height": 1.7, "weight": 50.5},   # Skarmory
    238: {"height": 0.6, "weight": 6.0},    # Smoochum
    239: {"height": 0.6, "weight": 23.5},   # Elekid
    240: {"height": 0.7, "weight": 20.7},   # Tyrogue
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

print("\n✓ All remaining fixes applied!")
