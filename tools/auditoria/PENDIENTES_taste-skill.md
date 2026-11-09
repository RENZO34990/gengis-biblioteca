# Pendientes de diseño: lo obtenido de taste-skill (nov 2026)

Fuente: fork RENZO34990/taste-skill (design-taste-frontend, high-end-visual-design, redesign-existing-projects). Auditoría estática de 4 páginas y búsquedas en las 52 páginas. Nada de esto está aplicado todavía. Los Design DNA de China, Japón y Corea siguen cerrados.

## 1. Ya cumplido (no hacer nada)
- Sin `window.addEventListener('scroll')` en ninguna página.
- Todas las fuentes de Google cargan con `display=swap`.
- Sin textos de "Scroll" como señal decorativa.
- Sin `transition: all`, sin ease-in/linear; solo `transform` y `opacity` en movimiento nuevo.
- `prefers-reduced-motion` respetado.
- Sin `#000` puro; solo 1 página con `#fff` puro (portal u otra, revisar).
- Fuentes propias de cada país (Hanken, Zen Kaku, Gothic A1, Atkinson): no están prohibidas.

## 2. Aplicable sin tocar el diseño (bajo riesgo)
1. Metadatos: `meta description`, `og:title`, `og:description`, `og:image` y favicon en 52 páginas (hoy no hay ninguno).
2. `font-variant-numeric: tabular-nums` en cifras y tablas.
3. `text-wrap: balance` en titulares y `text-wrap: pretty` en párrafos.
4. Skip-link, `<main>` y `<nav>` en cuadernos (el portal ya los tiene); `aria-current` en navegación.
5. `404.html` con estilo Kongzhi.
6. Imágenes con `width` y `height` (CLS < 0.1).
7. `min-height:100dvh` donde haya alturas de pantalla completa (hoy no se usa `100vh`).
8. `overflow-wrap` para títulos largos en kanji y hangul.
9. Ordenar `z-index: 999` del portal.
10. Del audit de animación: retardos de entrada del hero (1,5 a 1,9 s, bajar a ~0,6 s) y scrub 1,2 (probar 0,6).
11. Medir con Lighthouse: LCP < 2,5 s, INP < 200 ms, CLS < 0,1.

## 3. Requiere decisión de Renzo (choca con el estilo actual)
- **Guion largo (—) y semirraya (–):** la skill pide cero. Hoy hay unos 6 a 13 guiones largos y varias semirrayas en rangos (1839–1842) por cuaderno. Opciones: cero absoluto, o solo eliminar en titulares, etiquetas y pies de foto, dejándolo en el cuerpo.
- **Punto medio (·):** la skill lo raciona (máx. 1 por línea). Lo usamos en créditos y eyebrows ("Kongzhi · País · Política"). 
- **Tres columnas iguales:** `.flat-grid{repeat(3,1fr)}` en cada cuaderno; la skill lo prohíbe como fila de features. Revisar si es una cuadrícula de datos legítima.
- **Hero:** máx. 4 elementos de texto. Nuestro hero tiene eyebrow, título, subtítulo y la lista de cifras (aprobada por Renzo). Decidir si se mantiene.
- **Modo oscuro:** la skill lo exige. Los DNA están diseñados sobre papel claro. Decidir si se hace una versión oscura o no.
- **Fuentes autoalojadas:** la skill desaconseja `<link>` a Google Fonts. Mejora la privacidad y la carga, pero es un cambio de infraestructura.
- **Eyebrows y etiquetas:** máx. 1 eyebrow por 3 secciones; sin numeraciones tipo "Acto 01 / 05" como eyebrow. Choca con la estructura en 5 actos.
- **Candado de tema:** una sola paleta de página. Los héroes oscuros sobre cuerpo claro se podrían contar como inversión.

## 4. No aplicar (fuera de alcance)
React/Next/Tailwind/Motion, sistemas de diseño oficiales, generación de imágenes, muros de logos, bento, glassmorphism, nav flotante en píldora, grano, tipografía obligatoria sans: contradicen los DNA o no son nuestra pila. Los dashboards del observatorio Gengis quedan fuera del alcance de esta skill.

## 5. Regla permanente
Antes de entregar cualquier cuaderno o cambio del portal: auditoría de animación (Emil Kowalski) más esta lista, con la protección de la sección 11.F de la skill: no cambiar slugs, anclas, etiquetas de navegación ni logotipo sin aprobación.
