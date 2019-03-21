from http.server import HTTPServer, BaseHTTPRequestHandler
import ast
from io import BytesIO
from twitter_bot import tweet_temp


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        r = body.decode('ascii')
        r = ast.literal_eval(r)
        temp = r.get("temp")
        print(temp)
        tweet = "The temperature in the laboratory is above the threshold. It's " + temp + ' ' + u'\N{DEGREE SIGN}' + 'C'
        tweet_temp(tweet)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
