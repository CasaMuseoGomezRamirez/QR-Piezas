# QR-Piezas · Casa Museo Gómez Ramírez

Páginas web estáticas (una por pieza del museo) alojadas en GitHub Pages. Cada pieza tiene una URL fija que se imprime como código QR junto a la pieza.

- **Sitio:** https://casamuseogomezramirez.github.io/QR-Piezas/
- **Registro de piezas y URL:** [`QR.md`](QR.md)
- **Plan y decisiones de diseño:** [`Plan.md`](Plan.md)

## Estructura

```
QR-Piezas/
├─ piezas/<slug>/          Una carpeta por pieza: index.html + foto.jpg
├─ qr/QR-<slug>.png|.svg   Código QR de cada pieza (listo para imprimir)
├─ assets/                 estilo.css, logo-cgr.png e iconos.md (compartidos por todas las piezas)
├─ plantilla/index.html    Punto de partida para una pieza nueva
├─ fuentes/                Fichas/infografías originales (imágenes de referencia)
├─ herramientas/           nueva_pieza.py · verificar.py · servir.py
├─ QR.md                   Tabla pieza ↔ URL ↔ QR
├─ REQUISITOS-IMPRESION-QR.md  Qué se puede y qué no antes de imprimir un QR
├─ 404.html  .nojekyll     Página de error y desactivación de Jekyll (no tocar)
└─ index.html              Portada mínima (los QR no apuntan aquí)
```

## Reglas que no se rompen

1. **La URL de una pieza impresa no cambia nunca.** No renombres ni muevas `piezas/<slug>/`, ni el repo, ni la organización. Si hay que reorganizar, deja en la ruta antigua un `index.html` con redirección (`<meta http-equiv="refresh" content="0; url=NUEVA_URL">`).
2. **Slug:** minúsculas, números y guiones, sin tildes ni espacios (`minipiano-eavestaff`). Corto y descriptivo: URL más corta = QR más simple de escanear.
3. **Rutas relativas** (`../../assets/estilo.css`), nunca absolutas con `/`: así funciona igual en local y bajo `/QR-Piezas/` en GitHub Pages. La única excepción son `og:image`, `og:url` y `canonical`, que deben ser URL completas.
4. **Nada de textos solo dentro de imágenes.** El texto se escribe en HTML (accesible, buscable, escala bien en móvil).
5. **Nombre de los archivos de QR:** siempre `QR-<slug de la pieza>` (p. ej. `QR-minipiano-eavestaff.png` y `.svg`), dentro de `qr/`. No se usan otros nombres ni se guardan QR fuera de esa carpeta. El script `nueva_pieza.py` ya los nombra así y `verificar.py` lo comprueba.
6. **Todo QR se prueba con un celular** y se revisa contra [`REQUISITOS-IMPRESION-QR.md`](REQUISITOS-IMPRESION-QR.md) antes de imprimir.

## Crear una pieza nueva (paso a paso)

**Preparación (una sola vez):** `pip install -r requirements.txt` (necesita Python 3).

1. **Reúne el material:** la ficha o infografía (guárdala en `fuentes/<slug>.png`) y una foto de la pieza en buena resolución (idealmente ≥ 1000 px de ancho, vertical o cuadrada).
2. **Crea la pieza** desde la carpeta del repo:
   ```powershell
   python herramientas/nueva_pieza.py mi-pieza --nombre "Nombre de la pieza" --titulo "Título grande" --foto C:\ruta\foto.jpg
   ```
   Esto crea `piezas/mi-pieza/` con la plantilla, la foto optimizada (`foto.jpg`), el QR en `qr/QR-mi-pieza.png` y `.svg`, y añade la fila a `QR.md`.
3. **Escribe el contenido** en `piezas/mi-pieza/index.html`: introducción, sello (`<div class="sello-años">`), tarjetas (`<section class="tarjeta">`, cada una con `<h2>` y `<ul>`) y frase de cierre. Copia el texto de la ficha. Iconos en [`assets/iconos.md`](assets/iconos.md). Escribe un `alt` descriptivo en la foto.
4. **Míralo en local:**
   ```powershell
   python herramientas/servir.py
   ```
   Abre `http://localhost:8000/QR-Piezas/piezas/mi-pieza/`. Prueba con el modo móvil del navegador (F12 → icono de móvil) en 320, 360, 390 y 430 px: no debe haber scroll horizontal ni elementos montados.
5. **Verifica:** `python herramientas/verificar.py` (marcadores sin reemplazar, archivos faltantes, fila en `QR.md`, QR existente, `alt` en imágenes).
6. **Sube:**
   ```powershell
   git add -A
   git commit -m "Añade pieza: <nombre>"
   git push
   ```
7. **Espera 1–2 minutos** a que Pages publique (pestaña *Actions* del repo) y abre la URL pública.
8. **Escanea el QR** (`qr/QR-mi-pieza.png`) con un celular. Si abre la página correcta, actualiza en `QR.md` el estado a `Publicada` y haz commit/push.
9. **Imprime** el QR (ver abajo).

> Hacer las cosas a mano también vale: copiar `plantilla/` a `piezas/<slug>/`, reemplazar los `{{MARCADORES}}`, añadir `foto.jpg`, generar el QR y añadir la fila a `QR.md`.

## Imprimir el QR

La lista completa de lo permitido y lo prohibido está en [`REQUISITOS-IMPRESION-QR.md`](REQUISITOS-IMPRESION-QR.md); es obligatoria antes de cada impresión. Resumen:

- Usa preferentemente el **SVG** (escala sin perder nitidez). El PNG es de 1140 px.
- Tamaño mínimo recomendado: **2.5 × 2.5 cm**; para leer a 1 m de distancia, unos 8 cm.
- Respeta el **margen blanco** alrededor (4 módulos) y no pongas logos encima: el QR ya usa corrección de errores nivel H.
- Fondo claro y QR oscuro, con buen contraste; evita superficies brillantes que reflejen luz.
- Imprime una prueba y escanéala con varios celulares antes de la tirada definitiva.

## Estilo y diseño

- Todo el estilo está en `assets/estilo.css`. Cambiarlo afecta a **todas** las piezas: revisa al menos dos antes de publicar un cambio.
- Paleta: vinotinto `#6b0f1a`, oro `#c9a14a`, crema `#fbf1dc`. Fuentes: Great Vibes (título), Cinzel (rótulos), Cormorant Garamond (texto).
- Diseño pensado para móvil: una sola columna, ancho máximo 560 px. Los títulos de tarjeta van dentro de la tarjeta, sin posiciones absolutas ni márgenes negativos, para que nunca se monten sobre el texto.

## Publicación (GitHub Pages)

Configurado en *Settings → Pages → Deploy from a branch → `main` / `(root)`*. Todo se publica desde `main`. Si algo no aparece, revisa la pestaña *Actions* y recarga sin caché (Ctrl+F5).

## Mantenimiento y respaldo

- Conserva copia de `qr/` y `fuentes/` (ya están en el repo; haz además una copia local o en Drive).
- Cambiar el texto de una pieza ya publicada es seguro: la URL no cambia. Solo se vuelve a hacer commit y push.
- **A futuro (opcional, recomendado si el museo crece):** un dominio propio (p. ej. `piezas.tudominio.org`) con archivo `CNAME`. Permitiría cambiar de hosting sin reimprimir ningún QR. Hay que decidirlo **antes** de imprimir muchos QR, porque cambiar el dominio después implica reimprimir.
- Cuentas: el repo pertenece a la organización `CasaMuseoGomezRamirez`. Asegura que al menos dos personas tengan rol de propietario.
- Las páginas cargan fuentes de Google Fonts; si no estuvieran disponibles se ve una tipografía serif de respaldo y todo sigue funcionando.
