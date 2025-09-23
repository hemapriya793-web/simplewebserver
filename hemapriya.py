from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
   <title>table</title>
    </head>
    <boby>
        <h1 align="center">Device specification(HEMAPRIYA S)(25017270)</h1>
        <table border="10" cellpadding="20">
        <tr>
            <td>s.no</td>
            <td>device specification</td>
            <td>type</td>
        </tr>
        <tr>
            <td>1</td>
            <td>hemapriya</td>
            <td>TMP215-75-G2</td>
        </tr>
        <tr> 
            <td>2</td>
            <td>dhana</td>
            <td>processor</td>
        </tr>
        <tr>
            <td>3</td>
            <td>vashu</td>
            <td>product ID</td>
        </tr>
        <tr>
            <td>4</td>
            <td>sanju</td>
            <td>system type</td>
        </tr>
        <tr>
            <td>5</td>
            <td>priya</td>
            <td>installed RAM</td>
        </tr>


    </boby>
    </head>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
