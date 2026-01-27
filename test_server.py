import random
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys

print("Starting import...")
sys.path.insert(0, os.path.dirname(__file__))
from pokemon_data import POKEMON_DATA, get_pokemon_info_local
print(f"Imported {len(POKEMON_DATA)} pokemon")

class SimpleHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[LOG] {format % args}", flush=True)
    
    def do_GET(self):
        print(f">>> do_GET called for {self.path}", flush=True)
        if self.path == '/':
            self.path = '/index.html'
        
        # Try to serve from templates
        file_path = os.path.join(os.path.dirname(__file__), 'templates', self.path.lstrip('/'))
        if os.path.exists(file_path):
            print(f"    Serving file: {file_path}", flush=True)
            with open(file_path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        else:
            print(f"    File not found: {file_path}", flush=True)
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        print(f">>> do_POST called for {self.path}", flush=True)
        
        if self.path != '/api/generate':
            print(f"    Wrong path, returning 404", flush=True)
            self.send_response(404)
            self.end_headers()
            return
        
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            print(f"    Content-Length: {content_length}", flush=True)
            
            body = self.rfile.read(content_length)
            print(f"    Read {len(body)} bytes", flush=True)
            
            data = json.loads(body.decode('utf-8'))
            print(f"    Parsed JSON: {data}", flush=True)
            
            count = int(data.get('count', 3))
            print(f"    Count: {count}", flush=True)
            
            # Get pokemon
            all_names = list(POKEMON_DATA.keys())
            selected = random.sample(all_names, min(count, len(all_names)))
            print(f"    Selected: {selected}", flush=True)
            
            results = []
            for name in selected:
                info = get_pokemon_info_local(name)
                if info:
                    results.append(info)
                    print(f"      Added {name}", flush=True)
            
            print(f"    Total results: {len(results)}", flush=True)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'pokemon': results})
            self.wfile.write(response.encode('utf-8'))
            print(f"    Response sent ({len(response)} bytes)", flush=True)
            
        except Exception as e:
            print(f"    EXCEPTION: {e}", flush=True)
            import traceback
            traceback.print_exc()
            self.send_response(500)
            self.end_headers()

# Start server
print("\nStarting server...", flush=True)
server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
print("Server listening on 0.0.0.0:8000", flush=True)
server.serve_forever()
