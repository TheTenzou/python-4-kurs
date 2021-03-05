# from http.server import HTTPServer
# from http.server import BaseHTTPRequestHandler

# class ServerWorking(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/html')
#         self.end_headers()
#         self.wfile.write(bytes("<html><head><title>Title</title></head>", "utf-8"))
#         self.wfile.write(bytes("<body><h1>Python is working</h1>", "utf-8"))
#         self.wfile.write(bytes("</body></html>", "utf-8"))

from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()