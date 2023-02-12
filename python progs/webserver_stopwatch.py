"""
1. Create a HTTP webserver engine.
2. Add a stopwatch webpage.
3. Add to the webpage a start and stop button.
4. Display elapsed time.
"""


# Solution

# 1. Create a HTTP webserver engine.
import http.server

# 2. Add a stopwatch webpage.
# Create a simple HTML page

html_page = """
<html>
    <head>
        <title>Stopwatch</title>
    </head>
    <body>
        <h1>Stopwatch</h1>
        <p>Elapsed time: <span id="elapsed"></span></p>
        <button id="start">Start</button>
        <button id="stop">Stop</button>
        <script>
            // 3. Add to the webpage a start and stop button.
            let startButton = document.getElementById("start");
            let stopButton = document.getElementById("stop");
            let elapsedTime = document.getElementById("elapsed");

            let startTime = null;
            let interval = null;
            let elapsed = 0;

            startButton.addEventListener("click", () => {
                startTime = Date.now();
                interval = setInterval(() => {
                    elapsed = Date.now() - startTime;
                    // 4. Display elapsed time.
                    elapsedTime.innerHTML = elapsed / 1000;
                }, 1000);
            });

            stopButton.addEventListener("click", () => {
                clearInterval(interval);
            });
        </script>
    </body>
</html>
"""

# Create a handler for the page
class StopwatchRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(html_page.encode())

# Create the server and start it
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, StopwatchRequestHandler)
httpd.serve_forever()

