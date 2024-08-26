import ssl
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer


class SDKTestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"Ciao {self.address_string()}, hai inviato una GET!".encode())
        self.wfile.write(b"<br>")
        self.wfile.write(f"Sono le ore {datetime.now()}".encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            f"Ciao {self.address_string()}, hai inviato una POST!".encode()
        )


def run_server(*, port, server_class=HTTPServer, handler_class=SDKTestHandler):

    httpd = server_class(("", port), handler_class)

    # SSL context for HTTPS.
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="127.0.0.1.pem", keyfile="127.0.0.1-key.pem")
    httpd.socket = context.wrap_socket(
        httpd.socket,
        server_side=True,
    )

    httpd.serve_forever()


def main() -> None:
    run_server(port=8000)


if __name__ == "__main__":
    main()