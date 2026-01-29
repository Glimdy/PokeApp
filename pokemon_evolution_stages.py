"""
Pokemon Evolution Stage Database
Loads phase information from text files in the Pokemon Phases directory
"""

import os
from pokemon_data import POKEMON_DATA

def load_phases_from_text_files():
    """Load Pokemon evolution phases from text files in Pokemon Phases directory"""
    phases_dict = {}
    base_dir = os.path.dirname(__file__)
    phases_dir = os.path.join(base_dir, 'Pokemon Phases')
    
    # Map phase names to numeric values
    phase_map = {
        'Base': 1,
        'Phase 1': 2,
        'Phase 2': 3
    }
    
    # Read all generation files
    for gen in range(1, 10):
        file_path = os.path.join(phases_dir, f'gen{gen}.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    # Parse format: "Pokemon Name - Phase"
                    if ' - ' in line:
                        pokemon_name, phase_text = line.rsplit(' - ', 1)
                        pokemon_name = pokemon_name.strip()
                        phase_text = phase_text.strip()
                        
                        # Get the phase number
                        phase_num = phase_map.get(phase_text, 1)
                        
                        # Find the Pokemon ID from POKEMON_DATA
                        if pokemon_name in POKEMON_DATA:
                            pokemon_id = POKEMON_DATA[pokemon_name]['id']
                            phases_dict[pokemon_id] = phase_num
    
    return phases_dict

# Load phases from text files
POKEMON_EVOLUTION_STAGES = load_phases_from_text_files()

# Overrides for legendaries, mythicals, and special evolution lines that
# should not be treated as mid/final stages.
EVOLUTION_STAGE_OVERRIDES = {
    # Gen 1
    144: 1, 145: 1, 146: 1, 150: 1, 151: 1,
    # Gen 2
    243: 1, 244: 1, 245: 1, 249: 1, 250: 1, 251: 1,
    # Gen 3
    276: 1, 277: 2,  # Taillow, Swellow
    377: 1, 378: 1, 379: 1, 380: 1, 381: 1, 382: 1, 383: 1, 384: 1, 385: 1, 386: 1,
    # Gen 4
    480: 1, 481: 1, 482: 1, 483: 1, 484: 1, 485: 1, 486: 1, 487: 1, 488: 1,
    489: 1, 490: 1, 491: 1, 492: 1, 493: 1,
    # Gen 5
    494: 1, 638: 1, 639: 1, 640: 1, 641: 1, 642: 1, 643: 1, 644: 1, 645: 1,
    646: 1, 647: 1, 648: 1, 649: 1,
    # Gen 6
    716: 1, 717: 1, 718: 1, 719: 1, 720: 1, 721: 1,
    # Gen 7
    785: 1, 786: 1, 787: 1, 788: 1,
    789: 1, 790: 2, 791: 3, 792: 3,  # Cosmog line
    793: 1, 794: 1, 795: 1, 796: 1, 797: 1, 798: 1, 799: 1, 800: 1,
    801: 1, 802: 1, 803: 1, 804: 2, 805: 1, 806: 1, 807: 1,
    808: 1, 809: 2,  # Meltan line
    # Gen 8
    888: 1, 889: 1, 890: 1, 891: 1, 892: 2, 893: 1, 894: 1, 895: 1, 896: 1,
    897: 1, 898: 1,
    # Gen 9
    905: 1, 999: 1, 1000: 2, 1001: 1, 1002: 1, 1003: 1, 1004: 1,
    1007: 1, 1008: 1, 1025: 1,
}

def get_evolution_stage(pokemon_id):
    """Get the evolution stage for a given pokemon ID"""
    if pokemon_id in EVOLUTION_STAGE_OVERRIDES:
        return EVOLUTION_STAGE_OVERRIDES[pokemon_id]
    return POKEMON_EVOLUTION_STAGES.get(pokemon_id, 1)

def get_evolution_stage_name(stage):
    """Convert numeric stage to friendly name"""
    stage_names = {
        1: "Base",
        2: "Stage 1", 
        3: "Stage 2"
    }
    return stage_names.get(stage, "Unknown")
