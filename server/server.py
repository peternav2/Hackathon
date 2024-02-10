from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        
        # parsing 
        data = {}
        for param in body.split('&'):
            key, value = param.split('=')
            data[key] = value
        
        location = data.get('location', '')
        
        # Perform logic to get the competition 
        competition = get_competition(location)
        
        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(competition.encode('utf-8'))

def get_competition(location):

    return 'testing'

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()

run_server()