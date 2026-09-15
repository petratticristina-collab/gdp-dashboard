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
| `memoria/Curso_PotencIA_materiales_sesiones.md` | Lenguaje y técnicas del programa potencIA (M2 prompts y casos, Sesión III investigación, M4/Sesión IV diagnóstico): copiloto no piloto, pensamiento crítico sintético, ciclo de 6 pasos, rúbrica fidelidad/priorización/calibración/confusores/acción segura, máquinas no deterministas creando deterministas, escalera chatbot→razonador→agente. | 2026-09-11 |

Cuando la usuaria aporte material nuevo "para tener en memoria", añadirlo a `memoria/` como Markdown estructurado, registrarlo en esta tabla y hacer commit.

## Proyectos en curso
- `proyectos/libro_IA_AP_obesidad/`: el libro *IA en la consulta: la revolución que cabe en diez minutos* (Dra. Cristina Petratti), escrito capítulo a capítulo con el orquestador editorial. **Al retomar el proyecto ("sigue con mi libro"), leer primero `biblia.md`** (memoria compartida: decisiones, reglas, estado de capítulos, preguntas abiertas) y después el plan y el consolidado del último capítulo en `revisiones/`. Estado el 15-09-2026: **el libro tiene 10 capítulos (decisión de la autora del 15-09-2026; reagrupación de los antiguos 8-14 en 8, 9 y 10, ver decisión 1 de la biblia)**; capítulos 1-3 y 5 aprobados por la autora; 4 y 6 terminados y pendientes de su aprobación; 7 en ciclo. Cada ciclo produce `capitulos/capNN_v1.md` → cuatro informes en `revisiones/` → `capNN_consolidado.md` → `capNN_v2.md` → `capNN_v3_estilo.md` → PDF con `herramientas/md_a_pdf.py` (requiere `pip install markdown` y el Chromium de Playwright). `prompt_gemini.md` es el prompt maestro original para Gemini.
- `proyectos/orquestadores/`: dos sistemas multiagente con prompts de sistema, esquema de traspaso JSON y mapa de nodos n8n. `orquestador_editorial.md` (libro, 7 agentes) y `orquestador_contenido.md` (reels y posts, 6 agentes). Si la usuaria pide ejecutar uno, lanzar los agentes con la herramienta Agent siguiendo esos prompts y el ciclo descrito.

## Proyectos en curso (cont.)
- `proyectos/potencia_presentacion/`: presentación del proyecto final del programa potencIA (calculadora de condición física, 7 puntos de la plantilla del curso), generada con `build_deck.js`. Charla el lunes 14-09-2026.
- **Calculadora funcional:** repositorio público `adrsuarez22/calculadora-funcional` (app Streamlit `evaluacion-funcional-pro.streamlit.app`, 3 pruebas: caminata 6 min, prensión, silla; fuentes STAAB 2024, Tomkinson 2024, EXERNET 2012). Diagnóstico del 2026-09-11: interpolación por décadas en caminata, etiqueta errónea bajo P10 en silla, sin disclaimer ni población visible, dependencia supabase sin uso. Clonada en `/home/user/adrsuarez22/calculadora-funcional` (solo lectura en esta sesión).

## Estilo de respuesta preferido por la usuaria
Creativa, auténtica, científica y profesional. Responder en español.

## Proyecto
App Streamlit de ejemplo (`streamlit_app.py`) con datos de PIB en `data/`. Ejecutar con `streamlit run streamlit_app.py`.
