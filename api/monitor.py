from http.server import BaseHTTPRequestHandler
import time

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        try:
            while True:
                # Simulasi data monitoring
                data = f"data: CPU Usage: {round(time.time() % 100)}%\n\n"
                self.wfile.write(data.encode())
                self.wfile.flush()
                time.sleep(1)
        except:
            pass  # Koneksi ditutup oleh klien
