"""
Quick fix for known Pokemon size discrepancies
Based on official Pokedex data
"""

known_corrections = {
    208: {"name": "Steelix", "height": 8.8, "weight": 400.0},  # Was 0.9, 300.0
    95: {"name": "Onix", "height": 8.8, "weight": 213.0},  # Was 8.8 already, but check weight
    130: {"name": "Gyarados", "height": 6.5, "weight": 235.0},  # Check these
    149: {"name": "Dragonite", "height": 2.2, "weight": 210.0},  # Check these
    131: {"name": "Lapras", "height": 2.5, "weight": 220.0},  # Check these
    105: {"name": "Marowak", "height": 1.0, "weight": 45.0},  # Check weight
    103: {"name": "Exeggutor", "height": 2.0, "weight": 120.0},  # Check weight  
    110: {"name": "Weezing", "height": 1.2, "weight": 9.5},  # Alolan might be different
    227: {"name": "Skarmory", "height": 1.7, "weight": 50.5},  # Check
    226: {"name": "Mantine", "height": 2.1, "weight": 220.0},  # Check
    232: {"name": "Wooper", "height": 1.1, "weight": 35.0},  # Check
    238: {"name": "Smoochum", "height": 0.6, "weight": 6.0},  # Check
    222: {"name": "Corsola", "height": 0.6, "weight": 5.0},  # Check
    239: {"name": "Elekid", "height": 0.6, "weight": 23.5},  # Check
    240: {"name": "Tyrogue", "height": 0.7, "weight": 20.7},  # Check
    246: {"name": "Larvitar", "height": 0.6, "weight": 35.8},  # Check
}

# Print out what needs to be checked
print("Known problematic Pokemon:")
for pid, info in known_corrections.items():
    print(f"ID {pid}: {info['name']} - H: {info['height']}m, W: {info['weight']}kg")
