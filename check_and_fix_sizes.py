"""
Script to verify and fix Pokemon heights and weights against official Pokedex data
"""
import json
import requests
from pokemon_data import POKEMON_DATA

# Fetch official data from PokéAPI
def get_official_data():
    """Fetch all Pokemon data from PokéAPI"""
    official_data = {}
    
    for pokemon_id in range(1, 1026):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
            if response.status_code == 200:
                data = response.json()
                official_data[pokemon_id] = {
                    'name': data['name'],
                    'height': data['height'] / 10,  # Convert decimeters to meters
                    'weight': data['weight'] / 10   # Convert hectograms to kg
                }
                print(f"✓ Fetched {data['name']} (ID: {pokemon_id})")
            else:
                print(f"✗ Failed to fetch Pokemon ID {pokemon_id}")
        except Exception as e:
            print(f"✗ Error fetching Pokemon ID {pokemon_id}: {e}")
    
    return official_data

def compare_and_report(official_data):
    """Compare official data with current database"""
    from pokemon_extra_data import POKEMON_EXTRA_DATA
    
    discrepancies = []
    
    for pokemon_id, official_info in official_data.items():
        if pokemon_id not in POKEMON_EXTRA_DATA:
            discrepancies.append({
                'id': pokemon_id,
                'name': official_info['name'],
                'type': 'missing',
                'official_height': official_info['height'],
                'official_weight': official_info['weight']
            })
        else:
            current = POKEMON_EXTRA_DATA[pokemon_id]
            official = official_info
            
            height_diff = abs(current['height'] - official['height'])
            weight_diff = abs(current['weight'] - official['weight'])
            
            if height_diff > 0.1 or weight_diff > 1.0:  # Tolerance for rounding
                discrepancies.append({
                    'id': pokemon_id,
                    'name': official_info['name'],
                    'type': 'mismatch',
                    'current_height': current['height'],
                    'official_height': official['height'],
                    'height_diff': height_diff,
                    'current_weight': current['weight'],
                    'official_weight': official['weight'],
                    'weight_diff': weight_diff
                })
    
    return discrepancies

def generate_fixes(discrepancies):
    """Generate Python code to fix discrepancies"""
    fixes = []
    
    for disc in discrepancies:
        if disc['type'] == 'mismatch':
            fix_line = f"    {disc['id']}: {{'height': {disc['official_height']}, 'weight': {disc['official_weight']}, 'color': POKEMON_EXTRA_DATA[{disc['id']}]['color']}},  # {disc['name']} - fixed"
            fixes.append({
                'id': disc['id'],
                'name': disc['name'],
                'old_height': disc.get('current_height'),
                'new_height': disc['official_height'],
                'old_weight': disc.get('current_weight'),
                'new_weight': disc['official_weight'],
                'code': fix_line
            })
    
    return fixes

if __name__ == "__main__":
    print("Fetching official Pokemon data from PokéAPI...")
    print("=" * 60)
    official_data = get_official_data()
    
    print("\n" + "=" * 60)
    print("Comparing with current database...")
    print("=" * 60)
    
    discrepancies = compare_and_report(official_data)
    
    mismatches = [d for d in discrepancies if d['type'] == 'mismatch']
    missing = [d for d in discrepancies if d['type'] == 'missing']
    
    print(f"\nFound {len(mismatches)} height/weight mismatches")
    print(f"Found {len(missing)} missing Pokemon entries")
    
    if mismatches:
        print("\n" + "=" * 60)
        print("MISMATCHES (Top 10):")
        print("=" * 60)
        for disc in mismatches[:10]:
            print(f"\n{disc['name']} (ID: {disc['id']})")
            print(f"  Height: {disc['current_height']}m → {disc['official_height']}m (diff: {disc['height_diff']}m)")
            print(f"  Weight: {disc['current_weight']}kg → {disc['official_weight']}kg (diff: {disc['weight_diff']}kg)")
    
    # Save detailed report
    with open('size_discrepancies_report.json', 'w') as f:
        json.dump({
            'mismatches': mismatches,
            'missing': missing,
            'summary': {
                'total_mismatches': len(mismatches),
                'total_missing': len(missing)
            }
        }, f, indent=2)
    
    print(f"\n✓ Full report saved to size_discrepancies_report.json")
    
    # Generate fixes
    fixes = generate_fixes(mismatches)
    
    if fixes:
        print(f"\n✓ Generated {len(fixes)} fixes")
        print("\nTo apply fixes, update pokemon_extra_data.py with these values:")
        print("=" * 60)
        for fix in fixes[:5]:
            print(f"ID {fix['id']} ({fix['name']}):")
            print(f"  {fix['code']}")
