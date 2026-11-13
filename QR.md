# Registro de QR — Casa Museo Gómez Ramírez

Base de las URL: `https://casamuseogomezramirez.github.io/QR-Piezas/`

> **Regla de oro:** una vez impreso un QR, su URL **no se cambia nunca**. Si se reorganiza el repo, se deja la carpeta antigua con una redirección.

| N.º | Pieza | Carpeta (slug) | URL del QR | Estado |
|----|-------|----------------|-----------|--------|
| 1 | Minipiano Eavestaff y su banqueta “Ministool” | `piezas/minipiano-eavestaff/` | https://casamuseogomezramirez.github.io/QR-Piezas/piezas/minipiano-eavestaff/ | Publicada. QR: `qr/minipiano-eavestaff.png` / `.svg` |

## Cómo añadir una pieza
Guía completa en [`README.md`](README.md#crear-una-pieza-nueva-paso-a-paso). Resumen:

```powershell
python herramientas/nueva_pieza.py <slug> --nombre "Nombre" --titulo "Título" --foto rutaoto.jpg
python herramientas/verificar.py
git add -A; git commit -m "Añade pieza: <nombre>"; git push
```
Después de publicar, escanear el QR con un celular y cambiar el estado a `Publicada`.

Estados: `Borrador (sin publicar)` → `Publicada` → `QR impreso (fecha)`.
