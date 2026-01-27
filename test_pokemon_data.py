#!/usr/bin/env python3
"""Test that specific Pokemon have correct data"""

from pokemon_data import POKEMON_DATA

test_pokemon = [
    ('Pikachu', 25, ['Electric'], 1),
    ('Charizard', 6, ['Fire', 'Flying'], 1),
    ('Greninja', 658, ['Water', 'Dark'], 6),
    ('Koraidon', 1007, ['Fighting', 'Dragon'], 9),
    ('Miraidon', 1008, ['Electric', 'Dragon'], 9),
    ('Pecharunt', 1025, ['Poison', 'Ghost'], 9),
    ('Mewtwo', 150, ['Psychic'], 1),
    ('Arceus', 493, ['Normal'], 4),
    ('Rayquaza', 384, ['Dragon', 'Flying'], 3),
]

print("Testing sample Pokemon data:\n")
all_correct = True

for name, expected_id, expected_types, expected_gen in test_pokemon:
    if name in POKEMON_DATA:
        data = POKEMON_DATA[name]
        id_match = data['id'] == expected_id
        type_match = data['types'] == expected_types
        gen_match = data['generation'] == expected_gen
        
        status = "✓" if (id_match and type_match and gen_match) else "✗"
        print(f"{status} {name}: ID {data['id']} (expect {expected_id}), Types {data['types']}, Gen {data['generation']}")
        
        if not (id_match and type_match and gen_match):
            all_correct = False
    else:
        print(f"✗ {name}: NOT FOUND")
        all_correct = False

print(f"\n{'✓ All tests passed!' if all_correct else '✗ Some tests failed!'}")
print(f"Total Pokemon in database: {len(POKEMON_DATA)}")
