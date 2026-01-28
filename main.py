import random
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import unicodedata

# Import pokemon data
sys.path.insert(0, os.path.dirname(__file__))
from pokemon_data import POKEMON_DATA, get_pokemon_info_local
from pokemon_evolution_stages import get_evolution_stage, get_evolution_stage_name
from official_pokemon_data import OFFICIAL_POKEMON_DATA
from pokemon_habitat import get_habitat, get_habitat_translation
from habitat_icons import get_habitat_icon, get_habitat_emoji, get_habitat_svg

# Global game state
current_game_pokemon = None

def remove_accents(text):
    """Remove accents from text for flexible matching (e.g., électhor -> electhor)"""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def get_pokemon_by_generation(generation=None):
    """Get list of Pokemon names filtered by generation.
    
    Args:
        generation: Generation number (1-9) or None for all
        
    Returns:
        List of Pokemon names
    """
    if generation is None:
        return list(POKEMON_DATA.keys())
    
    try:
        gen = int(generation)
        if gen < 1 or gen > 9:
            return list(POKEMON_DATA.keys())
        
        filtered = []
        for name, data in POKEMON_DATA.items():
            if data.get('generation') == gen:
                filtered.append(name)
        return filtered
    except (ValueError, TypeError):
        return list(POKEMON_DATA.keys())

class PokemonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Serve static files from templates directory."""
        path = self.path
        
        # Handle API endpoints
        if path == '/api/pokemon-list':
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                pokemon_list = []
                for name in POKEMON_DATA.keys():
                    info = get_pokemon_info_local(name)
                    if info:
                        pokemon_list.append({'name': name, 'sprite': info['sprite']})
                self.wfile.write(json.dumps(pokemon_list).encode('utf-8'))
                return
            except Exception as e:
                print(f'Error in /api/pokemon-list: {e}', flush=True)
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
                return
        
        if path.startswith('/api/new-game'):
            try:
                # Parse generation parameter from query string
                generation = None
                if '?' in path:
                    query_string = path.split('?', 1)[1]
                    for param in query_string.split('&'):
                        if param.startswith('generation='):
                            generation = param.split('=', 1)[1]
                            break
                
                global current_game_pokemon
                # Get Pokemon list filtered by generation
                available_pokemon = get_pokemon_by_generation(generation)
                
                if not available_pokemon:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'No Pokemon available for selected generation'}).encode('utf-8'))
                    return
                
                current_game_pokemon = random.choice(available_pokemon)
                info = get_pokemon_info_local(current_game_pokemon)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    'name': current_game_pokemon,
                    'sprite': info['sprite'],
                    'generation': info['generation'],
                    'types': info['types']
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return
            except Exception as e:
                print(f'Error in /api/new-game: {e}', flush=True)
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
                return
        
        # Serve static files
        if path == '/':
            path = '/index.html'
        
        file_path = os.path.join(os.path.dirname(__file__), 'templates', path.lstrip('/'))
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Determine content type
            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'text/plain'
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Handle POST requests to /api/generate and /api/guess."""
        if self.path == '/api/generate':
            self.handle_generate()
        elif self.path == '/api/guess':
            self.handle_guess()
        else:
            self.send_response(404)
            self.end_headers()
    
    def handle_generate(self):
        """Handle the /api/generate endpoint."""
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            count = int(data.get('count', 3))
            generation_filter = data.get('generation')  # None or int
            type_filter = data.get('type')  # None or string
            
            # Validate count
            if count <= 0 or count > 50:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Count must be 1-50'}).encode('utf-8'))
                return
            
            # Filter pokemon by generation and/or type
            filtered_names = []
            for name, data in POKEMON_DATA.items():
                # Check generation filter
                if generation_filter is not None and data['generation'] != generation_filter:
                    continue
                
                # Check type filter
                if type_filter is not None and type_filter not in data['types']:
                    continue
                
                filtered_names.append(name)
            
            if len(filtered_names) == 0:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No Pokemon match the selected filters'}).encode('utf-8'))
                return
            
            # If requesting more than available, just return all available
            actual_count = min(count, len(filtered_names))
            
            # Select random pokemon from filtered list
            selected = random.sample(filtered_names, actual_count)
            
            # Get info for each pokemon
            results = []
            for name in selected:
                info = get_pokemon_info_local(name)
                if info:
                    # Add evolution stage info
                    pokemon_id = info.get('id', 1)
                    evolution_stage = get_evolution_stage(pokemon_id)
                    evolution_stage_name = get_evolution_stage_name(evolution_stage)
                    info['evolution_stage'] = evolution_stage
                    info['evolution_stage_name'] = evolution_stage_name
                    
                    # Add habitat info
                    habitat = get_habitat(pokemon_id)
                    habitat_name = get_habitat_translation(habitat, 'en')
                    habitat_icon = get_habitat_icon(habitat)
                    info['habitat'] = habitat
                    info['habitat_name'] = habitat_name
                    info['habitat_emoji'] = habitat_icon.get('emoji', '📍')
                    info['habitat_svg'] = habitat_icon.get('svg', '')
                    
                    results.append(info)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps({'pokemon': results})
            self.wfile.write(response.encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
    
    def handle_guess(self):
        """Handle the /api/guess endpoint for the game."""
        global current_game_pokemon
        
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            guess = data.get('guess', '').strip()
            
            if not guess:
                self.send_error_response('Please enter a Pokemon name')
                return
            
            # Check if pokemon exists (case-insensitive and accent-insensitive)
            guess_normalized = remove_accents(guess.lower())
            guess_pokemon = None
            for name in POKEMON_DATA.keys():
                if remove_accents(name.lower()) == guess_normalized:
                    guess_pokemon = name
                    break
            
            if not guess_pokemon:
                self.send_error_response(f'"{guess}" is not a valid Pokemon')
                return
            
            if not current_game_pokemon:
                self.send_error_response('No game in progress. Start a new game.')
                return
            
            # Get info for both pokemon
            guess_info = get_pokemon_info_local(guess_pokemon)
            target_info = get_pokemon_info_local(current_game_pokemon)
            
            if not guess_info or not target_info:
                self.send_error_response('Error retrieving Pokemon data')
                return
            
            # Get evolution stages
            guess_pokemon_id = guess_info.get('id', 1)
            target_pokemon_id = target_info.get('id', 1)
            guess_evolution_stage = get_evolution_stage(guess_pokemon_id)
            target_evolution_stage = get_evolution_stage(target_pokemon_id)
            guess_evolution_stage_name = get_evolution_stage_name(guess_evolution_stage)
            target_evolution_stage_name = get_evolution_stage_name(target_evolution_stage)
            
            # Get habitats
            guess_habitat = get_habitat(guess_pokemon_id)
            target_habitat = get_habitat(target_pokemon_id)
            guess_habitat_name = get_habitat_translation(guess_habitat, 'en')
            target_habitat_name = get_habitat_translation(target_habitat, 'en')
            guess_habitat_icon = get_habitat_icon(guess_habitat)
            target_habitat_icon = get_habitat_icon(target_habitat)
            
            # Detailed debug logging
            print(f'\n--- GUESS DEBUG ---', flush=True)
            print(f'Guess Pokemon: {guess_pokemon}', flush=True)
            print(f'Guess Info: {guess_info}', flush=True)
            print(f'Guess Height: {guess_info.get("height")}', flush=True)
            print(f'Guess Weight: {guess_info.get("weight")}', flush=True)
            print(f'Guess Color: {guess_info.get("color")}', flush=True)
            print(f'\n--- TARGET DEBUG ---', flush=True)
            print(f'Target Pokemon: {current_game_pokemon}', flush=True)
            print(f'Target Info: {target_info}', flush=True)
            print(f'Target Height: {target_info.get("height")}', flush=True)
            print(f'Target Weight: {target_info.get("weight")}', flush=True)
            print(f'Target Color: {target_info.get("color")}', flush=True)
            
            # Compare
            generation_match = guess_info['generation'] == target_info['generation']
            type1_match = guess_info['types'][0] == target_info['types'][0]
            type2_guess = guess_info['types'][1] if len(guess_info['types']) > 1 else None
            type2_target = target_info['types'][1] if len(target_info['types']) > 1 else None
            type2_match = type2_guess == type2_target
            
            # Height comparison
            height_guess = guess_info['height']
            height_target = target_info['height']
            if height_guess == height_target:
                height_value = "✓"
                height_match = True
            elif height_guess < height_target:
                height_value = "↑ Taller"
                height_match = False
            else:
                height_value = "↓ Shorter"
                height_match = False
            
            # Weight comparison
            weight_guess = guess_info['weight']
            weight_target = target_info['weight']
            if weight_guess == weight_target:
                weight_value = "✓"
                weight_match = True
            elif weight_guess < weight_target:
                weight_value = "↑ Heavier"
                weight_match = False
            else:
                weight_value = "↓ Lighter"
                weight_match = False
            
            # Color comparison
            color_match = guess_info['color'] == target_info['color']
            color_value = guess_info['color'].capitalize()
            
            correct = guess_pokemon == current_game_pokemon
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'correct': correct,
                'name': guess_pokemon,
                'sprite': guess_info['sprite'],
                'generation': {
                    'value': guess_info['generation_display'],
                    'match': generation_match
                },
                'evolution_stage': {
                    'value': guess_evolution_stage_name,
                    'match': guess_evolution_stage == target_evolution_stage
                },
                'type1': {
                    'value': guess_info['types'][0],
                    'match': type1_match
                },
                'type2': {
                    'value': type2_guess or '—',
                    'match': type2_match
                },
                'habitat': {
                    'value': guess_habitat_name,
                    'emoji': guess_habitat_icon.get('emoji', '📍'),
                    'match': guess_habitat == target_habitat
                },
                'height': {
                    'value': height_value,
                    'match': height_match
                },
                'weight': {
                    'value': weight_value,
                    'match': weight_match
                },
                'color': {
                    'value': color_value,
                    'match': color_match
                }
            }
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            print(f'Error in handle_guess: {e}', flush=True)
            self.send_error_response(str(e))
    
    def send_error_response(self, message):
        """Send an error response."""
        self.send_response(400)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'error': message}).encode('utf-8'))

def start_server(port=8000):
    """Start the Pokemon server."""
    handler = PokemonHandler
    server = HTTPServer(('0.0.0.0', port), handler)
    print(f'\nServer running on http://0.0.0.0:{port}')
    print(f'Access from browser at http://localhost:{port}\n')
    server.serve_forever()

if __name__ == '__main__':
    start_server()

