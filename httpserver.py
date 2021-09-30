import http.server
import socketserver
import requests

url="https://s2.qwant.com/thumbr/0x380/5/f/f255d2ccccce18e32b4e5dc8e3d55b1111e89200557bb745b6207194cffc2b/k1t6xac6k7u51.jpg?u=https%3A%2F%2Fi.redd.it%2Fk1t6xac6k7u51.jpg&q=0&b=1&p=0&a=0"

def run():
    PORT = 8001

    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    httpd.serve_forever()

    requests.get(url)

