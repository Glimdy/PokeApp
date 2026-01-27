#!/usr/bin/env python3
"""
Generate comprehensive Pokemon database from PokeAPI.
Fetches Pokemon directly from PokeAPI with correct IDs and data.
Excludes Mega Evolutions, Gigantamax, and similar alternate forms.
"""

import requests
import json
import time
from collections import defaultdict

# Forms to exclude
EXCLUDE_KEYWORDS = [
    'mega', 'gigantamax', 'gmax', 'eternamax', 'totem',
    'starter', 'cap', 'partner', 'world', 'original', 'belle', 
    'rock-star', 'libre', 'phd', 'pop-star', 'cosplay'
]

# Regional variants and forms we want to include
KEEP_KEYWORDS = [
    'alola', 'galar', 'hisui', 'paldea'
]

def should_exclude_pokemon(name, form_name):
    """Check if a Pokemon should be excluded based on its name or form."""
    full_name = f"{name} {form_name}".lower()
    
    # Check if it has a keep keyword - if so, include it
    for keep in KEEP_KEYWORDS:
        if keep in full_name:
            return False
    
    # Check for excluded keywords
    for exclude in EXCLUDE_KEYWORDS:
        if exclude in full_name:
            return True
    
    return False

def get_generation(pokemon_id):
    """Determine generation based on Pokemon ID."""
    if 1 <= pokemon_id <= 151:
        return 1
    elif 152 <= pokemon_id <= 251:
        return 2
    elif 252 <= pokemon_id <= 386:
        return 3
    elif 387 <= pokemon_id <= 493:
        return 4
    elif 494 <= pokemon_id <= 649:
        return 5
    elif 650 <= pokemon_id <= 721:
        return 6
    elif 722 <= pokemon_id <= 809:
        return 7
    elif 810 <= pokemon_id <= 905:
        return 8
    else:
        return 9

def fetch_all_pokemon():
    """Fetch all Pokemon from PokeAPI."""
    print("Fetching Pokemon data from PokeAPI...")
    
    # Disable SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    all_pokemon = {}
    
    # Get the total count first
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1', timeout=10, verify=False)
        total_count = response.json()['count']
        print(f"Total Pokemon available: {total_count}")
    except:
        total_count = 1025
        print(f"Using default count: {total_count}")
    
    # Fetch all Pokemon with a higher limit
    print("Fetching Pokemon list...")
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={total_count}', timeout=30, verify=False)
        pokemon_list = response.json()['results']
        print(f"Found {len(pokemon_list)} Pokemon")
    except Exception as e:
        print(f"Error fetching Pokemon list: {e}")
        return all_pokemon
    
    # Fetch details for each Pokemon
    print("Fetching detailed information...")
    for idx, pokemon in enumerate(pokemon_list, 1):
        try:
            # Add delay to avoid rate limiting
            if idx % 50 == 0:
                print(f"  Processed {idx}/{len(pokemon_list)}...")
                time.sleep(1)
            
            response = requests.get(pokemon['url'], timeout=10, verify=False)
            data = response.json()
            
            pokemon_id = data['id']
            pokemon_name = data['name']
            
            # Check forms - skip if it's an excluded form
            forms = data.get('forms', [])
            form_name = forms[0]['name'] if forms else pokemon_name
            
            if should_exclude_pokemon(pokemon_name, form_name):
                continue
            
            # Get types
            types = [t['type']['name'].capitalize() for t in data['types']]
            
            # Get species for better name
            species_url = data['species']['url']
            species_response = requests.get(species_url, timeout=10, verify=False)
            species_data = species_response.json()
            
            # Get English name
            display_name = pokemon_name.replace('-', ' ').title()
            for name_entry in species_data.get('names', []):
                if name_entry['language']['name'] == 'en':
                    display_name = name_entry['name']
                    break
            
            # Handle regional variants
            if '-' in pokemon_name:
                parts = pokemon_name.split('-')
                if any(keyword in pokemon_name for keyword in KEEP_KEYWORDS):
                    # Keep the variant name
                    display_name = pokemon_name.replace('-', ' ').title()
            
            generation = get_generation(pokemon_id)
            
            all_pokemon[display_name] = {
                'id': pokemon_id,
                'types': types,
                'generation': generation
            }
            
        except Exception as e:
            print(f"  Error processing {pokemon.get('name', 'unknown')}: {str(e)[:50]}")
            continue
    
    print(f"\nSuccessfully fetched {len(all_pokemon)} Pokemon!")
    return all_pokemon
def generate_pokemon_data_file(pokemon_dict):
    """Generate the pokemon_data.py file."""
    print("Generating pokemon_data.py...")
    
    # Sort by ID for proper ordering
    sorted_pokemon = sorted(pokemon_dict.items(), key=lambda x: x[1]['id'])
    
    # Generate the Python code
    code = '''"""
Comprehensive Pokemon database with ALL Pokemon across all generations.
Includes base forms and regional variants (Alola, Galar, Hisuian, Paldea).
Excludes: Mega Evolutions, Gigantamax, Dynamax, Totem forms.
Auto-generated from PokeAPI with correct National Pokedex IDs.
"""

POKEMON_DATA = {
'''
    
    for name, data in sorted_pokemon:
        # Escape quotes in name
        safe_name = name.replace('"', '\\"')
        code += f'    "{safe_name}": {{"id": {data["id"]}, "types": {data["types"]}, "generation": {data["generation"]}}},\n'
    
    code += '''}

def get_pokemon_sprite_url(pokemon_id):
    """Get sprite URL from GitHub official artwork"""
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"

def get_pokemon_info_local(name):
    """Get Pokemon info from local database"""
    if name in POKEMON_DATA:
        data = POKEMON_DATA[name]
        sprite_url = get_pokemon_sprite_url(data['id'])
        return {
            'name': name,
            'types': data['types'],
            'generation': f"Generation {data['generation']}",
            'sprite': sprite_url
        }
    return None
'''
    
    return code

def main():
    try:
        # Fetch all Pokemon
        pokemon_data = fetch_all_pokemon()
        
        if not pokemon_data:
            print("No Pokemon data fetched!")
            return
        
        # Generate file content
        file_content = generate_pokemon_data_file(pokemon_data)
        
        # Write to file
        output_path = 'pokemon_data.py'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        print(f"\nSuccessfully wrote {len(pokemon_data)} Pokemon to {output_path}")
        
        # Summary by generation
        by_gen = defaultdict(int)
        for data in pokemon_data.values():
            by_gen[data['generation']] += 1
        
        print("\nPokemon by generation:")
        for gen in sorted(by_gen.keys()):
            print(f"  Generation {gen}: {by_gen[gen]} Pokemon")
        
        # Show sample Pokemon
        print("\nSample Pokemon (first 5):")
        for name, data in sorted(pokemon_data.items(), key=lambda x: x[1]['id'])[:5]:
            print(f"  {name} (ID: {data['id']}, Types: {', '.join(data['types'])}, Gen: {data['generation']})")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
