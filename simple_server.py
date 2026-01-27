from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys
import random

# Import pokemon data
sys.path.insert(0, os.path.dirname(__file__))
from pokemon_data import POKEMON_DATA, get_pokemon_info_local

print(f"Loaded {len(POKEMON_DATA)} pokemon", flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello from GET</h1>")
    
    def do_POST(self):
        print(f">>> POST to {self.path}", flush=True)
        if self.path != '/api/generate':
            self.send_response(404)
            self.end_headers()
            return
        
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)
            count = int(data.get('count', 3))
            
            print(f"    Requested: {count}", flush=True)
            
            # Get pokemon
            all_names = list(POKEMON_DATA.keys())
            print(f"    Available: {len(all_names)}", flush=True)
            
            selected = random.sample(all_names, min(count, len(all_names)))
            print(f"    Selected: {selected}", flush=True)
            
            results = []
            for name in selected:
                print(f"      get_pokemon_info_local('{name}')", flush=True)
                info = get_pokemon_info_local(name)
                print(f"        -> {info is not None}", flush=True)
                if info:
                    results.append(info)
                else:
                    print(f"        -> RETURNED NONE!", flush=True)
            
            print(f"    Final results: {len(results)}", flush=True)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'pokemon': results})
            self.wfile.write(response.encode('utf-8'))
            print(f"    Sent {len(response)} bytes", flush=True)
        except Exception as e:
            print(f"ERROR: {e}", flush=True)
            import traceback
            traceback.print_exc()
            self.send_response(500)
            self.end_headers()

print("Starting pokemon server...")
server = HTTPServer(('0.0.0.0', 8000), Handler)
print("Listening on 8000")
server.serve_forever()
