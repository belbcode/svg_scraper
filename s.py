from http.server import HTTPServer, BaseHTTPRequestHandler
import s_svg_locator

class SVGServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if(self.path == 'GET /favicon.ico HTTP/1.1'):
            print('here')
            self.send_response(':(')
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        req_query = (self.path).split('%22')

        response = s_svg_locator(req_query[1])
        print(response)
        self.wfile.write(bytes(f"{req_query}", "utf-8"))   


def run(server_class=HTTPServer, handler_class=SVGServer):

    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()