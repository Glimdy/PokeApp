"""
Fetch official Pokemon height and weight data from PokéAPI
Includes all 1025 Pokemon from generations 1-9
"""

import requests
import json
from typing import List, Dict

def fetch_all_pokemon_data() -> List[Dict]:
    """
    Fetch official height and weight data for all 1025 Pokemon from PokéAPI
    Returns a list of dictionaries with: id, name, height (meters), weight (kg)
    """
    pokemon_data = []
    base_url = "https://pokeapi.co/api/v2/pokemon"
    
    print("Fetching official Pokemon data from PokéAPI...")
    print("This includes all generations (1-9) up to Pokemon #1025\n")
    
    # Fetch first 1025 Pokemon
    url = f"{base_url}?limit=1025"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        results = data.get('results', [])
        total = len(results)
        
        print(f"Found {total} Pokemon to fetch detailed data for...")
        
        # Fetch details for each Pokemon
        for idx, pokemon in enumerate(results, 1):
            if idx % 100 == 0:
                print(f"  Processing Pokemon {idx}/{total}...")
            
            pokemon_url = pokemon['url']
            try:
                poke_response = requests.get(pokemon_url, timeout=10)
                poke_response.raise_for_status()
                poke_data = poke_response.json()
                
                pokemon_data.append({
                    'id': poke_data['id'],
                    'name': poke_data['name'],
                    'height_dm': poke_data['height'],  # decimeters in API
                    'height_m': poke_data['height'] / 10,  # convert to meters
                    'weight_hg': poke_data['weight'],  # hectograms in API
                    'weight_kg': poke_data['weight'] / 10  # convert to kg
                })
            except requests.RequestException as e:
                print(f"  Error fetching Pokemon {pokemon['name']}: {e}")
                continue
        
        print(f"\nSuccessfully fetched data for {len(pokemon_data)} Pokemon!\n")
        return pokemon_data
    
    except requests.RequestException as e:
        print(f"Error fetching Pokemon list: {e}")
        return []


def format_as_csv(pokemon_data: List[Dict]) -> str:
    """Format data as CSV with proper headers"""
    if not pokemon_data:
        return ""
    
    csv_lines = ["Pokemon_ID,Name,Height_Meters,Weight_Kg"]
    
    for poke in sorted(pokemon_data, key=lambda x: x['id']):
        csv_lines.append(
            f"{poke['id']},{poke['name']},{poke['height_m']:.2f},{poke['weight_kg']:.1f}"
        )
    
    return "\n".join(csv_lines)


def format_as_json(pokemon_data: List[Dict]) -> str:
    """Format data as JSON"""
    if not pokemon_data:
        return "{}"
    
    # Sort by ID for consistent output
    sorted_data = sorted(pokemon_data, key=lambda x: x['id'])
    
    # Create a cleaner format for output
    clean_data = []
    for poke in sorted_data:
        clean_data.append({
            'id': poke['id'],
            'name': poke['name'],
            'height_m': round(poke['height_m'], 2),
            'weight_kg': round(poke['weight_kg'], 1)
        })
    
    return json.dumps(clean_data, indent=2)


def format_as_python_dict(pokemon_data: List[Dict]) -> str:
    """Format data as Python dictionary for easy import"""
    if not pokemon_data:
        return "{}"
    
    sorted_data = sorted(pokemon_data, key=lambda x: x['id'])
    
    lines = ["OFFICIAL_POKEMON_DATA = {"]
    for poke in sorted_data:
        lines.append(
            f"    {poke['id']}: {{'name': '{poke['name']}', 'height_m': {poke['height_m']:.2f}, 'weight_kg': {poke['weight_kg']:.1f}}},"
        )
    lines.append("}")
    
    return "\n".join(lines)


def main():
    """Main execution"""
    # Fetch data
    pokemon_data = fetch_all_pokemon_data()
    
    if not pokemon_data:
        print("Failed to fetch Pokemon data!")
        return
    
    # Save as CSV
    csv_content = format_as_csv(pokemon_data)
    with open('official_pokemon_data.csv', 'w', encoding='utf-8') as f:
        f.write(csv_content)
    print(f"✓ Saved CSV: official_pokemon_data.csv ({len(pokemon_data)} Pokemon)")
    
    # Save as JSON
    json_content = format_as_json(pokemon_data)
    with open('official_pokemon_data.json', 'w', encoding='utf-8') as f:
        f.write(json_content)
    print(f"✓ Saved JSON: official_pokemon_data.json")
    
    # Save as Python dict
    python_content = format_as_python_dict(pokemon_data)
    with open('official_pokemon_data.py', 'w', encoding='utf-8') as f:
        f.write(python_content)
    print(f"✓ Saved Python: official_pokemon_data.py")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY OF OFFICIAL POKEMON DATA")
    print("="*60)
    print(f"Total Pokemon fetched: {len(pokemon_data)}")
    print(f"ID Range: {min(p['id'] for p in pokemon_data)} - {max(p['id'] for p in pokemon_data)}")
    print(f"\nSmallest Pokemon: {min(pokemon_data, key=lambda x: x['height_m'])['name']} "
          f"({min(p['height_m'] for p in pokemon_data):.2f}m, "
          f"{min(p['weight_kg'] for p in pokemon_data):.1f}kg)")
    print(f"Largest Pokemon: {max(pokemon_data, key=lambda x: x['height_m'])['name']} "
          f"({max(p['height_m'] for p in pokemon_data):.2f}m, "
          f"{max(p['weight_kg'] for p in pokemon_data):.1f}kg)")
    print(f"Lightest Pokemon: {min(pokemon_data, key=lambda x: x['weight_kg'])['name']} "
          f"({min(p['weight_kg'] for p in pokemon_data):.1f}kg)")
    print(f"Heaviest Pokemon: {max(pokemon_data, key=lambda x: x['weight_kg'])['name']} "
          f"({max(p['weight_kg'] for p in pokemon_data):.1f}kg)")
    
    # Print sample of data
    print("\n" + "="*60)
    print("SAMPLE DATA (First 10 Pokemon)")
    print("="*60)
    print(f"{'ID':<5} {'Name':<20} {'Height (m)':<12} {'Weight (kg)':<12}")
    print("-"*60)
    for poke in sorted(pokemon_data, key=lambda x: x['id'])[:10]:
        print(f"{poke['id']:<5} {poke['name']:<20} {poke['height_m']:<12.2f} {poke['weight_kg']:<12.1f}")


if __name__ == "__main__":
    main()
