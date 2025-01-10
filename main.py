from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from collections import defaultdict
import threading

ip_freq = defaultdict(int)
lock = threading.Lock()  # To ensure thread safety


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        ip, _ = self.client_address

        with lock:
            ip_freq[ip] += 1

            print(f" BLOCKED IP : {ip_freq}")
            if ip_freq[ip] > 10:
                self.send_response(403)
                self.wfile.write(
                    "too may request, you have been blocked\n".encode("utf-8")
                )
                return 

        super().do_GET()


if __name__ == "__main__":
    os.chdir("./current_class")
    httpd = HTTPServer(("0.0.0.0", 8000), Handler)
    httpd.serve_forever()
