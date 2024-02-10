from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer
import json
# class CORSRequestHandler(BaseHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Access-Control-Allow-Methods', 'GET')
#         self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
#         return super(CORSRequestHandler, self).end_headers()
class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        SimpleHTTPRequestHandler.end_headers(self)
        return super(MyHTTPRequestHandler, self).end_headers()
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        body = json.loads(body)
        print(body)
        # parsing 
        
        # location = data.get('location', 'not found')
        
        # Perform logic to get the competition 
        competition = get_competition(body['location'])
        
        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(competition.encode('utf-8'))

def get_competition(location):
    print("Location: ", location)
    return location

def run_server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()

run_server()