from http.server import BaseHTTPRequestHandler, HTTPServer

def run(wyvernHandler, server_class=HTTPServer, port=8888):
    class RequestHandler(BaseHTTPRequestHandler):
        def _set_headers(self):
            wyvernHandler.setHeaders(self)

        def do_GET(self):
            wyvernHandler.doGET(self)

        def do_HEAD(self):
            wyvernHandler.doHEAD(self)

        def do_POST(self):
            wyvernHandler.doPOST(self)
    server_address = ('', port)
    httpd = server_class(server_address, RequestHandler)
    print('Starting httpd...')
    httpd.serve_forever()