# CLAUDE.md

## Memoria persistente del proyecto

La carpeta `memoria/` contiene conocimiento que la usuaria (Dra. Cristina Petratti) ha pedido mantener cargado y actualizado entre sesiones. **Finalidad declarada por la usuaria: esta memoria es la base para la construcción de reels y posteos sanitarios en redes sociales.** Leer estos archivos al inicio de cualquier tarea de creación, revisión o reformulación de contenido digital (reels, stories, carruseles, posts), colaboraciones con industria o farmacovigilancia. Empezar siempre por `memoria/M3_protocolo_creacion_reels_posts.md`, que encadena el resto en orden de producción.

| Archivo | Contenido | Última actualización |
|---|---|---|
| `memoria/M3_marco_legal_etico_compliance.md` | Módulo 3 del Programa de Líderes en divulgación científica digital: 7 líneas rojas de publicación, protocolo de farmacovigilancia en redes (3 pasos), 4 filtros + 3 disclaimers para colaborar con industria, marco normativo (RD 1416/1994, RD 577/2013, RGPD, Código Influencers 2025, Farmaindustria). | 2026-09-10 |
| `memoria/M3_checklist_compliance.md` | Checklist operativo del Módulo 3: 10 verificaciones en 4 áreas (competencia/propósito/caso clínico, consentimientos y licencias, disclosure con industria, pasada final), regla del minuto, protocolo RAM en 3 pasos con plantilla, puntuación de auditoría (8-10 / 6-7 / <6). Cita LOPS 44/2003, LOPDGDD, Código Deontológico OMC 2022 art. 199.2. | 2026-09-10 |
| `memoria/M3_guia_disclosure.md` | Guía de disclosure: cuándo declarar (regla del efecto vigente, tipos de vínculo), dónde (bio, post fijado anual, contenido específico), cómo (lenguaje concreto y trazable), acumulación con contenido patrocinado, test rápido de transparencia. | 2026-09-10 |
| `memoria/M3_tres_disclaimers.md` | Plantillas literales de los tres disclaimers (General, Referral, Patrocinado): cuándo, dónde, texto exacto, estándar de identificación comercial y regla de acumulación. | 2026-09-10 |
| `memoria/M3_regla_una_sola_persona.md` | Los tres checks de privacidad antes de publicar un caso clínico, cómo construir un arquetipo compuesto, requisitos de consentimiento, marco normativo en cadena (RGPD, LOPDGDD, OMC 2022, art. 199.2 Código Penal). | 2026-09-10 |
| `memoria/M3_dos_y_donts_posting.md` | Diez pares Do/Don't del posting sanitario en redes, reconstruidos en tabla, con mapa cruzado al resto del módulo. | 2026-09-10 |
| `memoria/M3_protocolo_creacion_reels_posts.md` | **Punto de entrada.** Flujo de producción de un reel/post en 6 fases (antes de escribir, guion, producción, disclosure, antes de publicar, después de publicar) que encadena los seis materiales del Módulo 3, más el formato de entrega exigido para cada pieza. | 2026-09-10 |
| `memoria/M3_ejercicio_practico_respuestas.md` | Ejercicio práctico evaluable del Módulo 3: enunciado resumido, rúbrica y respuestas a los cinco casos (conflicto no declarado, caso identificable, patrocinio mal etiquetado, RAM no notificada, consulta individualizada por DM). Sirve de modelo de razonamiento infracción → norma → corrección. | 2026-09-10 |
| `memoria/Programa_AI_Powered_Metabolic_Medicine.md` | Programa de IA generativa cursado por la usuaria (8 módulos: fundamentos y ética, prompt engineering médico, investigación, diagnóstico, audiovisual, agentes, día a día, proyecto final). Base del proyecto de libro en `proyectos/libro_IA_AP_obesidad/`. | 2026-09-10 |

Cuando la usuaria aporte material nuevo "para tener en memoria", añadirlo a `memoria/` como Markdown estructurado, registrarlo en esta tabla y hacer commit.

## Proyectos en curso
- `proyectos/libro_IA_AP_obesidad/prompt_gemini.md`: prompt maestro y secuencia de prompts para Gemini con los que la usuaria escribe un libro sobre IA en Atención Primaria para el abordaje de la obesidad. Al retomar el proyecto, leer primero ese archivo.
- `proyectos/orquestadores/`: dos sistemas multiagente con prompts de sistema, esquema de traspaso JSON y mapa de nodos n8n. `orquestador_editorial.md` (libro, 7 agentes) y `orquestador_contenido.md` (reels y posts, 6 agentes). Si la usuaria pide ejecutar uno, lanzar los agentes con la herramienta Agent siguiendo esos prompts y el ciclo descrito.

## Estilo de respuesta preferido por la usuaria
Creativa, auténtica, científica y profesional. Responder en español.

## Proyecto
App Streamlit de ejemplo (`streamlit_app.py`) con datos de PIB en `data/`. Ejecutar con `streamlit run streamlit_app.py`.
