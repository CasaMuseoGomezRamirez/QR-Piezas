# Plan — Páginas de piezas con QR (Casa Museo Gómez Ramírez)

## Objetivo
Convertir cada ficha ilustrada de una pieza (p. ej. `fuentes/minipiano-eavestaff.png`) en una página web estática, pensada primero para móvil, alojada en GitHub Pages. Cada pieza tiene una URL propia y estable que se codifica en un QR impreso.

- Repo: https://github.com/CasaMuseoGomezRamirez/QR-Piezas.git
- Sitio: https://casamuseogomezramirez.github.io/QR-Piezas/

## Estructura
```
QR-Piezas/
├─ index.html                 # portada mínima del sitio (no listada en los QR)
├─ assets/                    # CSS, logo e iconos compartidos
├─ piezas/<slug>/             # index.html + foto.jpg por pieza
├─ qr/                        # QR-<slug>.png y .svg de cada pieza
├─ REQUISITOS-IMPRESION-QR.md # lista de control antes de imprimir
├─ plantilla/                 # punto de partida de piezas nuevas
├─ herramientas/              # nueva_pieza.py, verificar.py, servir.py
├─ fuentes/                   # imágenes originales de las fichas
├─ QR.md                      # tabla pieza ↔ URL del QR
├─ README.md                  # guía operativa (cómo crear piezas)
└─ Plan.md
```

## Decisiones
- **HTML + CSS puro**, sin build ni frameworks: nada que se rompa con los años.
- **Mobile-first**: una columna, máx. 560 px, texto real (accesible, buscable), no la imagen incrustada.
- **URL duraderas**: slug corto, en minúsculas y sin tildes; jamás se renombra. Con barra final (`/`).
- Fuentes de Google (Great Vibes, Cinzel, Cormorant Garamond) con tipografías serif de respaldo.
- Imágenes recortadas de la ficha original; si hay fotos mejores, sustituir `foto.jpg`.

## Fases
1. [x] Estructura y recorte de imágenes.
2. [x] Página 1: Minipiano Eavestaff (`piezas/minipiano-eavestaff/`).
3. [x] `QR.md` con la URL de la pieza.
4. [x] Revisar en local en móvil (ancho 360–430 px) y ajustar.
5. [x] Commit y push al repo; activar Pages (Settings → Pages → rama `main`, carpeta `/root`).
6. [x] Probar la URL pública y generar el QR (nivel de corrección **H**, formato SVG/PNG alta resolución).
7. [x] Herramientas, plantilla y documentación para nuevas piezas (`README.md`).
8. [ ] Repetir para las demás piezas con `herramientas/nueva_pieza.py`.

## Sobre la perdurabilidad del QR
- El QR apunta al dominio `casamuseogomezramirez.github.io`; si la organización o el repo se renombran, la URL deja de funcionar. Mantener nombres.
- Opcional a futuro: dominio propio (p. ej. `piezas.casamuseo...`) con CNAME, para poder mover el hosting sin reimprimir QR.

## Ver en local
```
python herramientas/servir.py
# http://localhost:8000/QR-Piezas/piezas/minipiano-eavestaff/
```
