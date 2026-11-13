# Requisitos previos a la impresión de QR

Documento de control para los códigos QR de las piezas de la Casa Museo Gómez Ramírez. **Un QR impreso no se puede corregir**: si algo falla, hay que reimprimir. Revisa esta lista completa antes de cada impresión.

## 1. Qué es un QR en este proyecto

- Un QR guarda **una URL fija** de GitHub Pages: `https://casamuseogomezramirez.github.io/QR-Piezas/piezas/<slug>/`.
- El QR **no contiene** el contenido; solo la dirección. Por eso el **contenido de la página sí se puede cambiar** después de imprimir, pero **la dirección no**.

## 2. Qué SÍ se puede hacer (después de imprimir)

- Editar textos, fotos, estilos y datos de la página de la pieza (commit + push; la URL no cambia).
- Corregir errores de ortografía o de datos históricos.
- Añadir nuevas piezas y nuevos QR sin afectar a los anteriores.
- Reimprimir el mismo QR cuantas veces se quiera (el archivo `qr/QR-<slug>` no cambia).
- Cambiar el diseño de **todas** las páginas modificando `assets/estilo.css` (revisando antes dos piezas como mínimo).
- Redirigir una URL antigua a una nueva dejando en la ruta antigua un `index.html` con redirección.

## 3. Qué NO se puede hacer (rompe QR ya impresos)

- ✗ Renombrar o mover la carpeta `piezas/<slug>/`.
- ✗ Renombrar el repositorio `QR-Piezas` o la organización `CasaMuseoGomezRamirez` en GitHub.
- ✗ Borrar el repo, hacerlo privado o desactivar GitHub Pages.
- ✗ Cambiar de `github.io` a otro dominio **sin** dejar redirecciones en el sitio antiguo (y GitHub no permite mantener la redirección si se pierde la cuenta).
- ✗ Regenerar un QR con otra URL y mezclarlo con el anterior (un mismo objeto = un solo QR).
- ✗ Reutilizar un slug para otra pieza distinta.
- ✗ Poner **dos QR distintos** en la misma pieza.
- ✗ Modificar el QR a mano (recolorear con degradados, deformarlo, estirarlo, añadir logos encima, redondear los cuadros de las esquinas).
- ✗ Imprimir un QR que no haya sido probado con celular.

## 4. Nombre y ubicación de los archivos

- Todos los QR se llaman **`QR-<slug>`**: `QR-minipiano-eavestaff.png` y `QR-minipiano-eavestaff.svg`.
- Viven únicamente en `qr/`. No se guardan copias con otros nombres (`final`, `nuevo`, `copia`…): una sola versión vigente, el historial lo guarda git.
- Los genera `herramientas/nueva_pieza.py` (corrección de errores **H**, margen de 4 módulos). No se generan a mano con otras herramientas.
- El **slug** (nombre de carpeta y de QR): minúsculas, números y guiones; sin tildes, espacios ni mayúsculas.

## 5. Condiciones técnicas del QR

| Aspecto | Requisito |
|---|---|
| Corrección de errores | Nivel **H** (tolera ~30 % de daño o suciedad) |
| Margen blanco (zona de silencio) | Mínimo **4 módulos** (ya incluido en los archivos); no recortar |
| Colores | Módulos **oscuros** (negro o vinotinto muy oscuro) sobre fondo **claro**. Nunca invertido (claro sobre oscuro) ni con bajo contraste |
| Formato | **SVG** para imprenta/grabado; PNG (1140 px) para uso en pantalla o documentos |
| Tamaño mínimo impreso | **2.5 × 2.5 cm** (lectura a ~25 cm). Recomendado **4–5 cm** para vitrina o cartel; **8 cm** o más para leer a 1 m |
| Resolución en impresión | Mínimo 300 dpi si se usa PNG; con SVG no hay límite |
| Deformación | Proporción 1:1 exacta; no estirar ni rotar en 3D |
| Superficie | Mate, plana o con curvatura muy suave; evitar brillos, reflejos y vidrio sin antirreflejo delante |
| Iluminación | Que el QR no quede en sombra ni a contraluz de una ventana |

## 6. Control antes de imprimir (marcar todo)

- [ ] La URL de la pieza abre en el celular **desde internet** (no desde `localhost`).
- [ ] Contenido final revisado: textos, datos, ortografía y foto (nombre de la pieza correcto).
- [ ] La fila de la pieza en `QR.md` está completa y con estado `Publicada`.
- [ ] `python herramientas/verificar.py` termina en `OK`.
- [ ] El archivo del QR se llama `QR-<slug>` y está en `qr/`.
- [ ] El QR se escaneó con **al menos 2 celulares distintos** (uno Android y uno iPhone, si es posible) y abre la pieza correcta.
- [ ] Se imprimió una **prueba** al tamaño real y sobre el material real, y se escaneó a la distancia de uso.
- [ ] El texto junto al QR indica qué pieza es (por si el QR se daña) y, si aplica, la URL corta escrita en texto.
- [ ] Hay una copia de seguridad de `qr/` y `fuentes/` fuera del repositorio.
- [ ] Hay al menos **dos personas** con rol de propietario de la organización en GitHub.

## 7. Después de imprimir

- Actualiza el estado en `QR.md` a `QR impreso (AAAA-MM-DD)` y haz commit/push.
- Revisa cada cierto tiempo (p. ej. cada 6 meses) que las URL sigan respondiendo; conviene abrir todas las páginas de `QR.md`.
- Si un QR se daña o desgasta, reimprime el mismo archivo `QR-<slug>`: no se genera uno nuevo.
- Si cambias de dominio o de hosting en el futuro: mantén el sitio antiguo con redirecciones durante años, o planea reimprimir todo.

## 8. Decisión pendiente antes de la tirada grande

**Dominio propio.** Con `github.io`, el museo depende de que la organización y el repo conserven su nombre. Un dominio propio (p. ej. `piezas.dominio.org`, con un archivo `CNAME`) permitiría cambiar de hosting sin reimprimir. Si se va a adoptar, hay que hacerlo **antes** de imprimir muchos QR, porque cambiarlo después implica reimprimirlos.
