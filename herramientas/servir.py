"""Servidor local que imita GitHub Pages: el sitio queda bajo /QR-Piezas/.
Uso: python herramientas/servir.py  ->  http://localhost:8000/QR-Piezas/piezas/<slug>/"""
import http.server, functools, os
PREFIJO = "/QR-Piezas"
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path == PREFIJO: path += "/"
        if path.startswith(PREFIJO + "/"): path = path[len(PREFIJO):]
        return super().translate_path(path)
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
http.server.ThreadingHTTPServer(("", 8000), H).serve_forever()
