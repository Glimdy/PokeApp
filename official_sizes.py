"""
Official Pokemon heights and weights - from official Pokedex
All values in meters (height) and kilograms (weight)
"""

OFFICIAL_POKEMON_SIZES = {
    143: {"name": "Snorlax", "height": 2.1, "weight": 460.0},
    208: {"name": "Steelix", "height": 8.8, "weight": 400.0},
    95: {"name": "Onix", "height": 8.8, "weight": 213.0},
    130: {"name": "Gyarados", "height": 6.5, "weight": 235.0},
    149: {"name": "Dragonite", "height": 2.2, "weight": 210.0},
    147: {"name": "Dratini", "height": 1.8, "weight": 3.3},
    148: {"name": "Dragonair", "height": 4.0, "weight": 16.5},
    131: {"name": "Lapras", "height": 2.5, "weight": 220.0},
    105: {"name": "Marowak", "height": 1.0, "weight": 45.0},
    103: {"name": "Exeggutor", "height": 2.0, "weight": 120.0},
    110: {"name": "Weezing", "height": 1.2, "weight": 9.5},
    227: {"name": "Skarmory", "height": 1.7, "weight": 50.5},
    226: {"name": "Mantine", "height": 2.1, "weight": 220.0},
    232: {"name": "Wooper", "height": 1.1, "weight": 35.0},
    238: {"name": "Smoochum", "height": 0.6, "weight": 6.0},
    239: {"name": "Elekid", "height": 0.6, "weight": 23.5},
    240: {"name": "Tyrogue", "height": 0.7, "weight": 20.7},
    246: {"name": "Larvitar", "height": 0.6, "weight": 35.8},
    249: {"name": "Lugia", "height": 5.2, "weight": 216.0},
    250: {"name": "Ho-Oh", "height": 3.8, "weight": 199.0},
    330: {"name": "Flygon", "height": 2.0, "weight": 68.0},
    334: {"name": "Altaria", "height": 1.1, "weight": 20.6},
    371: {"name": "Bagon", "height": 0.6, "weight": 21.5},
    372: {"name": "Shelgon", "height": 1.1, "weight": 110.5},
    373: {"name": "Salamence", "height": 1.5, "weight": 102.2},
    374: {"name": "Beldum", "height": 0.6, "weight": 95.2},
    375: {"name": "Metang", "height": 1.2, "weight": 202.5},
    376: {"name": "Metagross", "height": 1.6, "weight": 550.0},
    384: {"name": "Rayquaza", "height": 7.0, "weight": 206.5},
    445: {"name": "Garchomp", "height": 1.9, "weight": 95.0},
    #Add more as needed - these are the most critical ones that are likely wrong
}

def get_size_fixes():
    """Load the official sizes"""
    return OFFICIAL_POKEMON_SIZES

if __name__ == "__main__":
    from pokemon_extra_data import POKEMON_EXTRA_DATA
    
    print("Checking for discrepancies:")
    print("=" * 70)
    
    for pokemon_id, official_info in OFFICIAL_POKEMON_SIZES.items():
        if pokemon_id in POKEMON_EXTRA_DATA:
            current = POKEMON_EXTRA_DATA[pokemon_id]
            height_match = abs(current['height'] - official_info['height']) < 0.1
            weight_match = abs(current['weight'] - official_info['weight']) < 1.0
            
            if not (height_match and weight_match):
                print(f"\n❌ {official_info['name']} (ID: {pokemon_id})")
                if not height_match:
                    print(f"   Height: {current['height']}m → {official_info['height']}m")
                if not weight_match:
                    print(f"   Weight: {current['weight']}kg → {official_info['weight']}kg")
            else:
                print(f"✓ {official_info['name']} (ID: {pokemon_id})")
