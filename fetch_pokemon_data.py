import requests
import time
import json

POKEMON_EXTRA_DATA = {}

print("Fetching Pokemon data from PokeAPI...")
print("This will take approximately 2-3 minutes...\n")

for pokemon_id in range(1, 1026):
    if pokemon_id % 100 == 0:
        print(f'Progress: {pokemon_id}/1025')
    
    height = 0.0
    weight = 0.0
    color = 'unknown'
    
    try:
        # Fetch Pokemon data
        pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/', timeout=5)
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()
            height = round(pokemon_data.get('height', 0) / 10, 1)
            weight = round(pokemon_data.get('weight', 0) / 10, 1)
    except Exception as e:
        pass
    
    try:
        # Fetch species data for color
        species_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/', timeout=5)
        if species_response.status_code == 200:
            species_data = species_response.json()
            color = species_data.get('color', {}).get('name', 'unknown')
    except Exception as e:
        pass
    
    POKEMON_EXTRA_DATA[pokemon_id] = {'height': height, 'weight': weight, 'color': color}
    time.sleep(0.03)

# Output the dictionary
print("\n" + "="*80)
print("POKEMON_EXTRA_DATA = {")
for pokemon_id in range(1, 1026):
    data = POKEMON_EXTRA_DATA[pokemon_id]
    print(f'    {pokemon_id}: {{"height": {data["height"]}, "weight": {data["weight"]}, "color": "{data["color"]}"}},')
print("}")
print("="*80)
