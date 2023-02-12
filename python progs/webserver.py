"""
1. Create a webserver engine
2. Add a webpage that is green
"""
print("View Webpage on a browser: http://localhost:8080/")

# Answer
#1. Create a webserver engine

from http.server import HTTPServer, BaseHTTPRequestHandler

class GreenWebPage(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<html><head><title>Green Webpage</title></head><body bgcolor="green"></body></html>')

httpd = HTTPServer(('localhost', 8080), GreenWebPage)
httpd.serve_forever()


