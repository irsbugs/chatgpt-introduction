"""
1. Create a HTTP webserver engine
2. Add a webpage.
3. Add to the webpage a form
4. The form has: first_name, surname, age fields
5. The form has a submit button
"""
print("View Webpage on a browser: http://localhost:8000/")

#Creating a HTTP webserver engine
from http.server import HTTPServer, BaseHTTPRequestHandler

#Creating a webpage
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<html><head><title>Welcome!</title></head>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<h1>Welcome to my site!</h1>')
        
        #Adding a form to the webpage
        self.wfile.write(b'<form method="POST" action="/form-results">')
        self.wfile.write(b'<label>First Name:</label>')
        self.wfile.write(b'<input type="text" name="first_name"/><br>')
        self.wfile.write(b'<label>Surname:</label>')
        self.wfile.write(b'<input type="text" name="surname"/><br>')
        self.wfile.write(b'<label>Age:</label>')
        self.wfile.write(b'<input type="number" name="age"/><br>')
        self.wfile.write(b'<input type="submit"/>')
        self.wfile.write(b'</form>')
        self.wfile.write(b'</body></html>')
        
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

        
