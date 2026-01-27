#!/usr/bin/env python3
"""
Complete Pokemon Database - All 1025 Pokemon
This contains the full National Pokedex database for generating pokemon_data.py
"""

# Complete database with all Pokemon 1-1025
# Format: (ID, Name, [Types], Generation)
COMPLETE_POKEMON_DATABASE = [
    # Gen 1 (1-151)
    (1, "Bulbasaur", ["Grass", "Poison"], 1), (2, "Ivysaur", ["Grass", "Poison"], 1), (3, "Venusaur", ["Grass", "Poison"], 1),
    (4, "Charmander", ["Fire"], 1), (5, "Charmeleon", ["Fire"], 1), (6, "Charizard", ["Fire", "Flying"], 1),
    (7, "Squirtle", ["Water"], 1), (8, "Wartortle", ["Water"], 1), (9, "Blastoise", ["Water"], 1),
    (10, "Caterpie", ["Bug"], 1), (11, "Metapod", ["Bug"], 1), (12, "Butterfree", ["Bug", "Flying"], 1),
    (13, "Weedle", ["Bug", "Poison"], 1), (14, "Kakuna", ["Bug", "Poison"], 1), (15, "Beedrill", ["Bug", "Poison"], 1),
    (16, "Pidgey", ["Normal", "Flying"], 1), (17, "Pidgeotto", ["Normal", "Flying"], 1), (18, "Pidgeot", ["Normal", "Flying"], 1),
    (19, "Rattata", ["Normal"], 1), (20, "Raticate", ["Normal"], 1), (21, "Spearow", ["Normal", "Flying"], 1),
    (22, "Fearow", ["Normal", "Flying"], 1), (23, "Ekans", ["Poison"], 1), (24, "Arbok", ["Poison"], 1),
    (25, "Pikachu", ["Electric"], 1), (26, "Raichu", ["Electric"], 1), (27, "Sandshrew", ["Ground"], 1),
    (28, "Sandslash", ["Ground"], 1), (29, "Nidoran F", ["Poison"], 1), (30, "Nidorina", ["Poison"], 1),
    (31, "Nidoqueen", ["Poison", "Ground"], 1), (32, "Nidoran M", ["Poison"], 1), (33, "Nidorino", ["Poison"], 1),
    (34, "Nidoking", ["Poison", "Ground"], 1), (35, "Clefairy", ["Fairy"], 1), (36, "Clefable", ["Fairy"], 1),
    (37, "Vulpix", ["Fire"], 1), (38, "Ninetales", ["Fire"], 1), (39, "Jigglypuff", ["Normal", "Fairy"], 1),
    (40, "Wigglytuff", ["Normal", "Fairy"], 1), (41, "Zubat", ["Poison", "Flying"], 1), (42, "Golbat", ["Poison", "Flying"], 1),
    (43, "Oddish", ["Grass", "Poison"], 1), (44, "Gloom", ["Grass", "Poison"], 1), (45, "Vileplume", ["Grass", "Poison"], 1),
    (46, "Paras", ["Bug", "Grass"], 1), (47, "Parasect", ["Bug", "Grass"], 1), (48, "Venonat", ["Bug", "Poison"], 1),
    (49, "Venomoth", ["Bug", "Poison"], 1), (50, "Diglett", ["Ground"], 1), (51, "Dugtrio", ["Ground"], 1),
    (52, "Meowth", ["Normal"], 1), (53, "Persian", ["Normal"], 1), (54, "Psyduck", ["Water"], 1),
    (55, "Golduck", ["Water"], 1), (56, "Mankey", ["Fighting"], 1), (57, "Primeape", ["Fighting"], 1),
    (58, "Growlithe", ["Fire"], 1), (59, "Arcanine", ["Fire"], 1), (60, "Poliwag", ["Water"], 1),
    (61, "Poliwhirl", ["Water"], 1), (62, "Poliwrath", ["Water", "Fighting"], 1), (63, "Abra", ["Psychic"], 1),
    (64, "Kadabra", ["Psychic"], 1), (65, "Alakazam", ["Psychic"], 1), (66, "Machop", ["Fighting"], 1),
    (67, "Machoke", ["Fighting"], 1), (68, "Machamp", ["Fighting"], 1), (69, "Bellsprout", ["Grass", "Poison"], 1),
    (70, "Weepinbell", ["Grass", "Poison"], 1), (71, "Victreebel", ["Grass", "Poison"], 1), (72, "Tentacool", ["Water", "Poison"], 1),
    (73, "Tentacruel", ["Water", "Poison"], 1), (74, "Geodude", ["Rock", "Ground"], 1), (75, "Graveler", ["Rock", "Ground"], 1),
    (76, "Golem", ["Rock", "Ground"], 1), (77, "Ponyta", ["Fire"], 1), (78, "Rapidash", ["Fire"], 1),
    (79, "Slowpoke", ["Water", "Psychic"], 1), (80, "Slowbro", ["Water", "Psychic"], 1), (81, "Magnemite", ["Electric", "Steel"], 1),
    (82, "Magneton", ["Electric", "Steel"], 1), (83, "Farfetch'd", ["Normal", "Flying"], 1), (84, "Doduo", ["Normal", "Flying"], 1),
    (85, "Dodrio", ["Normal", "Flying"], 1), (86, "Seel", ["Water"], 1), (87, "Dewgong", ["Water", "Ice"], 1),
    (88, "Grimer", ["Poison"], 1), (89, "Muk", ["Poison"], 1), (90, "Shellder", ["Water"], 1),
    (91, "Cloyster", ["Water", "Ice"], 1), (92, "Gastly", ["Ghost", "Poison"], 1), (93, "Haunter", ["Ghost", "Poison"], 1),
    (94, "Gengar", ["Ghost", "Poison"], 1), (95, "Onix", ["Rock", "Ground"], 1), (96, "Drowzee", ["Psychic"], 1),
    (97, "Hypno", ["Psychic"], 1), (98, "Krabby", ["Water"], 1), (99, "Kingler", ["Water"], 1),
    (100, "Voltorb", ["Electric"], 1), (101, "Electrode", ["Electric"], 1), (102, "Exeggcute", ["Grass", "Psychic"], 1),
    (103, "Exeggutor", ["Grass", "Psychic"], 1), (104, "Cubone", ["Ground"], 1), (105, "Marowak", ["Ground"], 1),
    (106, "Hitmonlee", ["Fighting"], 1), (107, "Hitmonchan", ["Fighting"], 1), (108, "Lickitung", ["Normal"], 1),
    (109, "Koffing", ["Poison"], 1), (110, "Weezing", ["Poison"], 1), (111, "Rhyhorn", ["Ground", "Rock"], 1),
    (112, "Rhydon", ["Ground", "Rock"], 1), (113, "Chansey", ["Normal"], 1), (114, "Tangela", ["Grass"], 1),
    (115, "Kangaskhan", ["Normal"], 1), (116, "Horsea", ["Water"], 1), (117, "Seadra", ["Water"], 1),
    (118, "Goldeen", ["Water"], 1), (119, "Seaking", ["Water"], 1), (120, "Staryu", ["Water"], 1),
    (121, "Starmie", ["Water", "Psychic"], 1), (122, "Mr. Mime", ["Psychic", "Fairy"], 1), (123, "Scyther", ["Bug", "Flying"], 1),
    (124, "Jynx", ["Ice", "Psychic"], 1), (125, "Electabuzz", ["Electric"], 1), (126, "Magmar", ["Fire"], 1),
    (127, "Pinsir", ["Bug"], 1), (128, "Tauros", ["Normal"], 1), (129, "Magikarp", ["Water"], 1),
    (130, "Gyarados", ["Water", "Flying"], 1), (131, "Lapras", ["Water", "Ice"], 1), (132, "Ditto", ["Normal"], 1),
    (133, "Eevee", ["Normal"], 1), (134, "Vaporeon", ["Water"], 1), (135, "Jolteon", ["Electric"], 1),
    (136, "Flareon", ["Fire"], 1), (137, "Porygon", ["Normal"], 1), (138, "Omanyte", ["Rock", "Water"], 1),
    (139, "Omastar", ["Rock", "Water"], 1), (140, "Kabuto", ["Rock", "Water"], 1), (141, "Kabutops", ["Rock", "Water"], 1),
    (142, "Aerodactyl", ["Rock", "Flying"], 1), (143, "Snorlax", ["Normal"], 1), (144, "Articuno", ["Ice", "Flying"], 1),
    (145, "Zapdos", ["Electric", "Flying"], 1), (146, "Moltres", ["Fire", "Flying"], 1), (147, "Dratini", ["Dragon"], 1),
    (148, "Dragonair", ["Dragon"], 1), (149, "Dragonite", ["Dragon", "Flying"], 1), (150, "Mewtwo", ["Psychic"], 1),
    (151, "Mew", ["Psychic"], 1),
]

# This file is incomplete - it only has Gen 1 for demonstration
# The complete database needs all generations 2-9 added
# For now, we'll reference the existing fix_pokemon_data.py which has more entries

if __name__ == "__main__":
    print(f"Complete database size: {len(COMPLETE_POKEMON_DATABASE)} Pokemon")
    print("NOTE: This is a placeholder - use fix_pokemon_data.py for the actual database generation")
