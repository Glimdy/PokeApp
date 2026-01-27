"""
Verification and comparison tool for Pokemon database
Compare your local Pokemon data against official PokéAPI data
"""

import json
import csv
from typing import List, Dict, Tuple

def load_official_data() -> Dict[int, Dict]:
    """Load official Pokemon data from JSON"""
    try:
        with open('official_pokemon_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Convert list to dictionary keyed by ID for easier lookup
            return {poke['id']: poke for poke in data}
    except FileNotFoundError:
        print("ERROR: official_pokemon_data.json not found. Run fetch_official_pokemon_data.py first.")
        return {}


def load_your_pokemon_data(file_path: str) -> Dict[int, Dict]:
    """Load Pokemon data from your database file"""
    your_data = {}
    
    try:
        # Try JSON format first
        if file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    your_data = {item['id']: item for item in data if 'id' in item}
                elif isinstance(data, dict):
                    your_data = data
        
        # Try CSV format
        elif file_path.endswith('.csv'):
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'Pokemon_ID' in row or 'id' in row:
                        id_key = 'Pokemon_ID' if 'Pokemon_ID' in row else 'id'
                        poke_id = int(row[id_key])
                        your_data[poke_id] = row
        
        # Try Python dict format
        elif file_path.endswith('.py'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract the dictionary (this is a simple approach)
                exec_globals = {}
                exec(content, exec_globals)
                for key, value in exec_globals.items():
                    if isinstance(value, dict) and key.isupper():
                        your_data = {int(k): v for k, v in value.items()}
                        break
    
    except Exception as e:
        print(f"ERROR loading file {file_path}: {e}")
        return {}
    
    return your_data


def compare_data(official: Dict[int, Dict], your_data: Dict[int, Dict]) -> Tuple[List[Dict], List[int], List[int]]:
    """
    Compare official data with your data
    Returns: (mismatches, missing_in_yours, missing_in_official)
    """
    mismatches = []
    missing_in_yours = []
    missing_in_official = []
    
    # Check for differences
    for poke_id, official_poke in official.items():
        if poke_id not in your_data:
            missing_in_yours.append(poke_id)
        else:
            your_poke = your_data[poke_id]
            
            # Normalize and compare heights
            official_height = official_poke.get('height_m')
            your_height = your_poke.get('height_m') or your_poke.get('height')
            
            if your_height is not None:
                try:
                    your_height = float(your_height)
                    if abs(official_height - your_height) > 0.01:  # Allow small floating point differences
                        mismatches.append({
                            'id': poke_id,
                            'name': official_poke.get('name'),
                            'field': 'height',
                            'official': official_height,
                            'yours': your_height
                        })
                except (ValueError, TypeError):
                    pass
            
            # Normalize and compare weights
            official_weight = official_poke.get('weight_kg')
            your_weight = your_poke.get('weight_kg') or your_poke.get('weight')
            
            if your_weight is not None:
                try:
                    your_weight = float(your_weight)
                    if abs(official_weight - your_weight) > 0.1:  # Allow small floating point differences
                        mismatches.append({
                            'id': poke_id,
                            'name': official_poke.get('name'),
                            'field': 'weight',
                            'official': official_weight,
                            'yours': your_weight
                        })
                except (ValueError, TypeError):
                    pass
    
    # Check for Pokemon in your data but not in official
    for poke_id in your_data:
        if poke_id not in official:
            missing_in_official.append(poke_id)
    
    return mismatches, missing_in_yours, missing_in_official


def print_comparison_report(official: Dict[int, Dict], your_data: Dict[int, Dict], 
                           mismatches: List[Dict], missing_in_yours: List[int], 
                           missing_in_official: List[int]):
    """Print detailed comparison report"""
    print("\n" + "="*80)
    print("POKEMON DATABASE VERIFICATION REPORT")
    print("="*80)
    
    print(f"\nData Coverage:")
    print(f"  Official Pokemon (PokéAPI): {len(official)}")
    print(f"  Your Pokemon: {len(your_data)}")
    
    if missing_in_yours:
        print(f"\n⚠ Missing from your database ({len(missing_in_yours)} Pokemon):")
        print(f"  IDs: {sorted(missing_in_yours)[:20]}", end="")
        if len(missing_in_yours) > 20:
            print(f" ... and {len(missing_in_yours) - 20} more")
        else:
            print()
    
    if missing_in_official:
        print(f"\n⚠ In your database but not in official ({len(missing_in_official)} Pokemon):")
        print(f"  IDs: {sorted(missing_in_official)}")
    
    if mismatches:
        print(f"\n❌ Data Mismatches ({len(mismatches)} found):")
        print(f"{'ID':<6} {'Name':<20} {'Field':<8} {'Official':<15} {'Yours':<15}")
        print("-"*80)
        
        for match in sorted(mismatches, key=lambda x: (x['id'], x['field']))[:50]:
            print(f"{match['id']:<6} {match['name']:<20} {match['field']:<8} "
                  f"{str(match['official']):<15} {str(match['yours']):<15}")
        
        if len(mismatches) > 50:
            print(f"... and {len(mismatches) - 50} more mismatches")
    
    if not mismatches and not missing_in_yours and not missing_in_official:
        print("\n✓ Your database matches official data perfectly!")
    
    print("\n" + "="*80)


def main():
    """Main execution"""
    print("Pokemon Database Verification Tool")
    print("="*80)
    
    # Load official data
    print("\nLoading official Pokemon data...")
    official_data = load_official_data()
    
    if not official_data:
        return
    
    print(f"✓ Loaded {len(official_data)} official Pokemon")
    
    # Ask user which file to check
    print("\nAvailable Pokemon database files:")
    import os
    pokemon_files = [f for f in os.listdir('.') if 'pokemon' in f.lower() 
                     and (f.endswith('.py') or f.endswith('.json') or f.endswith('.csv'))]
    
    for i, file in enumerate(pokemon_files, 1):
        print(f"  {i}. {file}")
    
    if not pokemon_files:
        print("  No Pokemon database files found!")
        return
    
    try:
        choice = int(input(f"\nSelect file to verify (1-{len(pokemon_files)}): "))
        if 1 <= choice <= len(pokemon_files):
            file_to_check = pokemon_files[choice - 1]
        else:
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid input!")
        return
    
    # Load and compare
    print(f"\nLoading your data from {file_to_check}...")
    your_data = load_your_pokemon_data(file_to_check)
    print(f"✓ Loaded {len(your_data)} Pokemon from {file_to_check}")
    
    print("\nComparing data...")
    mismatches, missing_in_yours, missing_in_official = compare_data(official_data, your_data)
    
    # Print report
    print_comparison_report(official_data, your_data, mismatches, missing_in_yours, missing_in_official)


if __name__ == "__main__":
    main()
