# Caso reservado para el capítulo 6 · Leer una etiqueta nutricional

> **Estado:** reservado para el capítulo 6 (educación grupal y preparación de material). Escrito y revisado dentro del ciclo del capítulo 2 (v1 → v2): ya pasó las cuatro revisiones (CLÍNICO, EVIDENCIA, COMPLIANCE, PROMPTS). Retirado del capítulo 2 por decisión del orquestador el 11-09-2026 para que ese capítulo quede con seis casos. Al integrarlo en el capítulo 6, renumerar el caso, reubicar las dos referencias del final en la lista del capítulo 6 y comprobar que la higiene de la herramienta (entrenamiento desactivado, borrar al terminar, versión vigente) se remite al capítulo 1 en vez de repetirse. El texto de abajo se conserva íntegro tal como salió de la v2 del capítulo 2; la pasada de estilo del capítulo 6 lo ajustará.

---

### Caso [n.º pendiente] · Leer una etiqueta nutricional

**Momento:** educación grupal y preparación de material (docencia). **Herramienta:** asistente multimodal, que lea imágenes.

**Situación.** "Esto es light, ¿no?" En la consulta, la etiqueta se lee juntos, con el dedo en la lista de ingredientes; ahí no hay móvil que valga. La IA sirve para preparar el taller o la hoja: diez etiquetas de letra diminuta convertidas en tablas en una tarde. Y "light" no es una opinión: la ley exige al menos un 30 % menos de algo respecto al producto de referencia (Reglamento 1924/2006). Lo que no dice es de qué, ni qué lleva a cambio.

**Antes de la foto.** De frente, sin flash, la tabla ocupando la pantalla; si el envase tiene dos tablas, dos fotos. El envase sobre una superficie lisa y neutra: sin manos, sin recetas, sin la pantalla del ordenador detrás y sin ninguna persona, sobre todo en una sala con gente. Los envases brillantes reflejan caras: míralo en grande antes de subirlo. Las fotos del móvil llevan dentro fecha, hora y, si se lo permites, dónde estabas; una captura de pantalla de la foto no las lleva: sube la captura. Al terminar, bórrala del carrete, de "eliminados recientemente" y de la nube, borra la conversación y, si hay biblioteca de archivos, el archivo. Borrar no deshace lo que el proveedor haya retenido: por eso la imagen tiene que poder verla cualquiera sin dañar a nadie.

```
ROL: Eres una dietista-nutricionista que lee etiquetas de alimentos envasados y transcribe lo que ve, sin valorarlo.

CONTEXTO: Te adjunto la imagen de la etiqueta de un producto envasado, hecha por mí y revisada antes de subirla. En la imagen no hay personas, ni manos, ni documentos, ni datos personales, y no debes inferir nada sobre quién lo consume. Es una transcripción para uso educativo; no sustituye a la etiqueta.

TAREA, en este orden:
(0) Legibilidad. Antes de transcribir nada, escribe una línea: "Legibilidad: BUENA / REGULAR / MALA". Si es MALA (números borrosos, brillos sobre la tabla, tabla cortada), escribe "REPETIR FOTO" y para. Si en la imagen aparece cualquier persona, parte del cuerpo, texto manuscrito, ticket o dirección, escribe "IMAGEN NO APTA" y para.
(1) Idioma y tablas. Di en qué idiomas está la etiqueta y cuántas tablas o columnas distintas hay (por 100 g o 100 ml; por ración; producto tal cual o preparado; con o sin leche; sin cocinar o cocinado). Usa la versión en español si existe; si no, indica el idioma que usas.
(2) Transcripción, una tabla por cada columna del envase, con el título que le da el envase, sin mezclarlas ni elegir una: energía (kJ y kcal), grasas, de las cuales saturadas, hidratos de carbono, de los cuales azúcares, fibra, proteínas, sal, y cualquier otra fila que figure. Copia los números con el mismo decimal y la misma unidad que ves. Si el envase imprime la columna %IR, cópiala; no calcules ninguna. Si un número o una palabra no se lee con claridad, escribe ILEGIBLE en esa casilla: no lo estimes ni lo completes con los valores habituales de ese tipo de producto.
(3) Lista de ingredientes, en su orden y con su texto exacto; si está en otro idioma, tradúcela al español dejando el original entre paréntesis.
(4) Los tres primeros ingredientes. Después, en dos listas separadas, las fuentes de azúcares y los edulcorantes que aparecen, contados y nombrados, solo de esta lista. Fuentes de azúcares: azúcar, sacarosa, glucosa, dextrosa, fructosa, jarabe o sirope (de glucosa, de glucosa-fructosa, de maíz, de agave, de arroz), miel, melaza, azúcar invertido, maltodextrina, zumo o concentrado de fruta añadido. Edulcorantes: sucralosa, aspartamo, acesulfamo K, sacarina, ciclamato, glucósidos de esteviol, polialcoholes (sorbitol, maltitol, xilitol, eritritol) o cualquier E-950 a E-969. Si ves otro que creas que es una fuente de azúcar, ponlo aparte con un interrogante.
(5) Comprobación aritmética, por cada tabla por 100 g o 100 ml: los azúcares no pueden superar a los hidratos, las saturadas no pueden superar a las grasas, y 4 × hidratos + 4 × proteínas + 9 × grasas + 2 × fibra debe quedar a menos de un 10 % de las kcal. Escribe "COHERENTE" o "INCOHERENTE: [qué no cuadra]" y, si es INCOHERENTE, la casilla que crees mal leída.

FORMATO: Las líneas (0) y (1); las tablas; la lista de ingredientes; el punto (4); la línea (5); y al final tres frases descriptivas en lenguaje llano, trato de usted, que digan qué lleva el producto y en qué cantidad por ración, sin valorarlo. Cierra las tres frases con esta línea literal: "Material informativo generado con apoyo de IA y revisado por su profesional sanitario. No sustituye la valoración clínica individual."

RESTRICCIONES: No digas si el producto es "bueno", "malo", "sano" o "light", ni si conviene a alguien. Sin consejos individuales, sin necesidades diarias, sin mencionar peso ni dietas. Sin nombres de marca: llama al producto por su tipo ("galleta de cereales", "yogur de sabores"). No conviertas unidades (sodio a sal, kJ a kcal, onzas a gramos): copia lo impreso.
```

**Ejemplo abreviado de salida.**

> Legibilidad: BUENA. Idiomas: español y portugués. Tablas: una (por 100 g y por ración de 30 g).
> Por 100 g: energía 1.890 kJ / 452 kcal; grasas 18 g, saturadas 8,2 g; hidratos 64 g, azúcares 23 g; fibra 3,1 g; proteínas 6,5 g; sal 0,9 g. Ración (30 g): azúcares 6,9 g.
> Ingredientes: harina de trigo, azúcar, aceite de palma […]. Fuentes de azúcares: azúcar, jarabe de glucosa (2). Edulcorantes: ninguno.
> Comprobación: 4×64 + 4×6,5 + 9×18 + 2×3,1 = 450 kcal frente a 452. COHERENTE.

**Qué revisar antes de usarla.** Los números, con la etiqueta delante: un 4,5 se lee como 45 con facilidad. Con legibilidad REGULAR, cuenta los ILEGIBLE: más de tres, repite la foto. INCOHERENTE casi siempre es un decimal mal leído. Que haya tantas tablas como tiene el envase: la que falta suele ser la que importa. El orden de los ingredientes es lo que de verdad informa: la normativa europea obliga a listarlos de mayor a menor peso (Reglamento 1169/2011, art. 18). "Azúcares añadidos" no existe en la etiqueta europea: lo deduces tú de la lista; por eso el prompt habla de fuentes de azúcares. Que las tres frases no se hayan deslizado hacia "es poco saludable": eso lo hablas tú, en el taller. Si las frases salen de tu boca, el disclaimer lo dices tú; si se imprimen o se envían, van con la frase literal del final y con tu nombre.

**Riesgo principal y mitigación.** Tres: un decimal mal leído; una imagen con más de lo que querías; y el más difícil de ver: cuando no lee un número, el modelo pone el valor habitual de ese tipo de producto, y parece una transcripción. Mitigación: la puerta de legibilidad, la comprobación aritmética, la etiqueta delante y la imagen revisada por ti, ampliada, antes de subirla. Cuando escribo esto, las versiones gratuitas de las tres grandes leen imágenes, y las tres fallan con brillos. Si una dice BUENA y luego llena la tabla de ILEGIBLE, repite la foto.

---

## Referencias que solo usa este caso (van a la lista del capítulo 6)

1. Reglamento (UE) n.º 1169/2011 del Parlamento Europeo y del Consejo, de 25 de octubre de 2011, sobre la información alimentaria facilitada al consumidor. Diario Oficial de la Unión Europea L 304, 22 de noviembre de 2011, p. 18-63. Art. 18. Disponible en: https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=celex%3A32011R1169
2. Reglamento (CE) n.º 1924/2006 del Parlamento Europeo y del Consejo, de 20 de diciembre de 2006, relativo a las declaraciones nutricionales y de propiedades saludables en los alimentos. Diario Oficial de la Unión Europea L 404, 30 de diciembre de 2006, p. 9-25. Anexo, declaración "light/lite". [VERIFICAR: referencia nueva en v2, no incluida en el informe de EVIDENCIA]
