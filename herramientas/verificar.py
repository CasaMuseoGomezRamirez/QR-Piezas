#!/usr/bin/env python
"""Revisa que todo esté coherente antes de hacer push.
Uso: python herramientas/verificar.py"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://casamuseogomezramirez.github.io/QR-Piezas/"
errores = []
qr_md = (RAIZ / "QR.md").read_text(encoding="utf-8")

for d in sorted((RAIZ / "piezas").iterdir()):
    if not d.is_dir():
        continue
    h = d / "index.html"
    if not h.exists():
        errores.append(f"{d.name}: falta index.html")
        continue
    t = h.read_text(encoding="utf-8")
    if "{{" in t:
        errores.append(f"{d.name}: quedan marcadores {{{{...}}}} sin reemplazar")
    if "Texto de introducción" in t or "Título de la tarjeta" in t or "Frase de cierre emotiva" in t:
        errores.append(f"{d.name}: queda texto de ejemplo de la plantilla")
    for ref in re.findall(r'(?:src|href)="(?!https?:|#|mailto:)([^"]+)"', t):
        if not (d / ref).resolve().exists():
            errores.append(f"{d.name}: no existe {ref}")
    if f"{BASE}piezas/{d.name}/" not in qr_md:
        errores.append(f"{d.name}: no está en QR.md")
    if not (RAIZ / "qr" / f"{d.name}.png").exists():
        errores.append(f"{d.name}: falta qr/{d.name}.png")
    if not re.search(r'<img[^>]+alt="[^"]+"', t):
        errores.append(f"{d.name}: imagen sin alt")

for e in errores:
    print("X", e)
print("OK: todo coherente" if not errores else f"{len(errores)} problema(s)")
sys.exit(1 if errores else 0)
