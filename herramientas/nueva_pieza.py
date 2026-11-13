#!/usr/bin/env python
"""Crea una pieza nueva: carpeta, página desde la plantilla, QR y fila en QR.md.

Uso:
  python herramientas/nueva_pieza.py <slug> --nombre "Nombre de la pieza" --titulo "Título grande" --foto ruta/foto.jpg

El slug es DEFINITIVO una vez impreso el QR (minúsculas, sin tildes, con guiones).
Requiere: pip install -r requirements.txt
"""
import argparse, re, sys
from pathlib import Path
from PIL import Image
import segno

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://casamuseogomezramirez.github.io/QR-Piezas/"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("slug")
    p.add_argument("--nombre", required=True, help="Nombre de la pieza (subtítulo guinda)")
    p.add_argument("--titulo", required=True, help="Título grande en cursiva")
    p.add_argument("--foto", help="Foto de la pieza (jpg/png); se optimiza a foto.jpg")
    p.add_argument("--descripcion", default="Casa Museo Gómez Ramírez.")
    a = p.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        sys.exit("Slug inválido: solo minúsculas, números y guiones (sin tildes ni espacios).")
    dest = RAIZ / "piezas" / a.slug
    if dest.exists():
        sys.exit(f"Ya existe {dest}. Nunca se sobrescribe una pieza publicada.")

    url = f"{BASE}piezas/{a.slug}/"
    dest.mkdir(parents=True)
    html = (RAIZ / "plantilla" / "index.html").read_text(encoding="utf-8")
    for k, v in {"URL": url, "TITULO": a.titulo, "NOMBRE": a.nombre, "DESCRIPCION": a.descripcion}.items():
        html = html.replace("{{" + k + "}}", v)
    (dest / "index.html").write_text(html, encoding="utf-8")

    if a.foto:
        im = Image.open(a.foto).convert("RGB")
        im.thumbnail((1200, 1600))
        im.save(dest / "foto.jpg", quality=85, optimize=True)
    else:
        print(f"AVISO: falta {dest / 'foto.jpg'}")

    (RAIZ / "qr").mkdir(exist_ok=True)
    q = segno.make(url, error="h")
    q.save(RAIZ / "qr" / f"QR-{a.slug}.svg", scale=10, border=4)
    q.save(RAIZ / "qr" / f"QR-{a.slug}.png", scale=20, border=4)

    md = RAIZ / "QR.md"
    lineas = md.read_text(encoding="utf-8").rstrip("\n").split("\n")
    filas = [i for i, l in enumerate(lineas) if re.match(r"\| \d+ \|", l)]
    n = len(filas) + 1
    fila = f"| {n} | {a.nombre} | `piezas/{a.slug}/` | {url} | Borrador (sin publicar). QR: `qr/QR-{a.slug}.png` |"
    lineas.insert(filas[-1] + 1, fila)
    md.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print(f"Creada: {dest}\nURL: {url}\nQR: qr/QR-{a.slug}.png")
    print("Siguiente: editar index.html, revisar en local, python herramientas/verificar.py")


main()
