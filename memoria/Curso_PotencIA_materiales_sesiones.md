# Memoria · Materiales de sesiones del programa potencIA / AI-Powered Metabolic Medicine

> **Fuentes:** guía de laboratorio del Módulo 2 (Consuelo Verdú, NCompany, junio 2026), deck de la Sesión III "IA para investigación" (Javier Fuentes), playbook del Módulo 4 "IA para el diagnóstico" y deck de la Sesión IV (Néstor Guerra, 25-jun-2026). Novo Nordisk 2026. Uso exclusivo para profesionales sanitarios.
> **Última actualización:** 2026-09-11.
> **Uso:** vocabulario y técnicas del curso para el libro, la presentación del proyecto final y cualquier pieza en la que la usuaria hable de cómo usa la IA.

## Frases y conceptos clave del programa (lenguaje del curso)
- **"La IA es copiloto, no piloto."** El modelo razona, estructura y redacta; el clínico verifica y firma. Si una salida parece demasiado segura, probablemente lo es. (M2, regla de oro)
- **"La gran mentira de llamar IA a todo."** IA gratuita, de pago, frontera, open source/local: no rinden igual. Pregunta correcta: *qué nivel de IA exige esta tarea*. Contrato mental: qué modelo, qué versión, qué plan, cuánto contexto, qué herramientas, cuál es el coste de error. (M4)
- **Pensamiento crítico sintético.** Usar la IA para generar perspectivas (explorador, integrador, auditor) y que el clínico decida qué síntesis conserva. "El valor no está en que la IA responda; está en que te obligue a formular mejor la pregunta." (M4)
- **Ciclo clínico de seis pasos:** representar → hipotetizar → contrastar → falsar → actualizar → auditar. Prompt base: "No cierres diagnóstico. Separa hechos, inferencias, datos ausentes, sesgos, conclusiones prematuras." (M4)
- **Sesgos que la IA amplifica:** anclaje, cierre prematuro, cascada, narrativa. "El modelo debe aprender a decir no lo sé con la misma claridad con la que escribe una hipótesis." (M4)
- **Rúbrica para leer una respuesta:** fidelidad · priorización · calibración · confusores · acción segura. (M4)
- **"Máquinas no deterministas creando máquinas deterministas."** El LLM es probabilístico; se usa para construir artefactos deterministas y verificables: checklists, formularios, dashboards, validadores, calculadoras. "La determinación no vive dentro del modelo. Vive en el proceso que le obligas a seguir." (M4) → **aplica directamente a la calculadora funcional de la usuaria.**
- **Markdown como conocimiento operativo:** caso, rúbrica, guía local, plantilla de salida; legible, versionable, dable al modelo como contexto. "No es magia documental." (M4)
- **Escalera de niveles (Bloomberg/OpenAI):** 1 chatbots → 2 razonadores → 3 agentes → 4 innovadores → 5 organizaciones. (S4)
- **Modelos frontera junio 2026 y su papel:** integrador clínico (contexto largo, trazabilidad) · auditor crítico (anclaje, cierre prematuro, cascada) · hipótesis paralelas (series temporales, modelos causales alternativos). Nota: LLM generalistas superan a herramientas clínicas especializadas en benchmarks médicos (Nature Medicine 2026). (M4/S4)

## Técnicas de prompt engineering médico (M2)
- Estructura **rol · contexto · tarea · formato · restricciones**; prompt pobre vs estructurado (ejercicio 1).
- **Few-shot** con documentos modelo propios anonimizados (cartas a AP, altas, interconsultas) para imitar estilo.
- **Cadena de prompts:** estructurar (sin opinar) → analizar dilemas con nivel de certeza → criticar (el modelo se revisa a sí mismo) → comunicar (doble salida: sesión clínica y familia).
- **Notas sueltas → SOAP** marcando huecos como [FALTA: …], sin inventar ni resolver ambigüedades.
- **Hoja de paciente multiidioma** con verificación por re-traducción en conversación nueva.
- **"Lost in the middle":** el dato enterrado a mitad de documento se pierde; dirigir la atención ("revisa el día 5 y 6") mejora la respuesta.
- Aviso de compliance del curso: casos sintéticos, anonimizar ejemplos propios, fármacos por principio activo o clase (arGLP-1, iSGLT2, iDPP4, insulinas basales), nunca por marca.

## Investigación con IA (Sesión III)
- Volumen: 800–1.200 papers/semana en endocrinología; >1.500 si se incluye diabetes, obesidad, nutrición.
- Itinerario: presentación → búsquedas por internet (Perplexity, ChatGPT Atlas) → búsqueda de evidencia (Consensus, Elicit, Scite, OpenEvidence, Claude) → exploración de literatura → consolidación → diseño de ensayos → cierre.
- Preguntas de investigación modelo en obesidad: predictores de respuesta al tratamiento farmacológico, criterios de selección, resultados a 6-12 meses en práctica real, respuesta ponderal precoz como predictor, beneficios más allá del IMC, pérdida de masa muscular y cómo prevenirla.
- "Hagamos un paper": flujo de redacción asistida con verificación de citas.

## Seguridad y datos (transversal)
- Nunca subir datos identificables a herramientas no cubiertas por contrato y política de seguridad; anonimizar y eliminar metadatos e imágenes.
- Las salidas dirigidas a pacientes requieren validación clínica y disclaimer.
- Checklist operativo de salida del taller (M4): definir nivel de IA, formato cerrado, rúbrica, verificación externa, revisión humana.
