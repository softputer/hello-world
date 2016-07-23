import BaseHTTPServer
import os
import socket

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/qingyuanos.png":
            hostname = socket.gethostname()
            message_parts = [
                "<html>",
                "<head><title>Hello World</title></head>",
                "<body style=\"text-align:center;\">",
                "<p><img src='qingyuanos.png' /></p>",
                "<h3>Hello QingYuanOS!</h3><br />",
                "<p>My hostname is <b>" + hostname + "</b></p>",
                "</body>",
                "<html>"
            ]
            message = '\r\n'.join(message_parts)
            # message = "New request arrived from %s:%d" % self.client_address
            self.send_response(200)
            self.end_headers()
            self.wfile.write(message)
