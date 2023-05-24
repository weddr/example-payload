from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Merhaba, bu bir örnek payload!"
        self.wfile.write(message.encode())

def run_server():
    host = 'localhost'
    port = 8000
    server = HTTPServer((host, port), MyHandler)
    print(f"Server {host}:{port} adresinde çalışıyor...")
    server.serve_forever()

run_server()
