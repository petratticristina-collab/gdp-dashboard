# Orquestadores de agentes · Dra. Cristina Petratti

Dos sistemas multiagente diseñados el 2026-09-10 sobre la anatomía enseñada en el Módulo 6 del programa *AI-Powered Metabolic Medicine*: cada agente tiene **cerebro** (el prompt de sistema), **memoria** (el archivo de estado que lee y escribe) y **herramientas** (lo que puede consultar). El orquestador no escribe contenido: planifica, reparte, verifica contratos de entrega y decide cuándo algo está terminado.

| Orquestador | Para qué | Archivo |
|---|---|---|
| **EDITORIAL** | Escribir el libro *IA en Atención Primaria para el abordaje de la obesidad*, capítulo a capítulo, con revisión clínica, de evidencia y de compliance en paralelo | `orquestador_editorial.md` |
| **CONTENIDO** | Producir reels, stories, carruseles y posts auditados con el Módulo 3, y gestionar comentarios y sospechas de RAM | `orquestador_contenido.md` |

## Tres formas de ejecutarlos, de menor a mayor automatización

1. **Manual con Gemas o Proyectos.** Una Gema (Gemini) o un Proyecto (Claude) por agente, con su prompt de sistema pegado en las instrucciones. Tú haces de "bus de mensajes": copias la salida JSON de un agente y la pegas en el siguiente. Cuesta cero infraestructura y sirve para aprender cómo se comportan.
2. **Semiautomático con un solo chat.** Pegas el prompt del ORQUESTADOR en un chat con contexto largo y le adjuntas los prompts de los agentes como archivos. El orquestador "interpreta" cada rol por turnos. Menos fiel, pero rápido para borradores.
3. **Automático con n8n.** Cada agente es un nodo *AI Agent* con su prompt de sistema; el orquestador es un nodo de decisión que enruta según el campo `estado` del JSON. Los archivos de memoria viven en Google Drive o Notion. Al final de cada archivo hay el mapa de nodos.

También puedo ejecutar cualquiera de los dos aquí mismo, en esta sesión, lanzando los agentes en paralelo sobre el repositorio: pídemelo con "ejecuta el orquestador editorial para el capítulo N" o "produce un reel sobre X".

## Reglas comunes a ambos
- **Un contrato de entrega por agente.** Cada agente devuelve un JSON con `agente`, `version`, `estado` (`ok` / `revisar` / `bloqueado`), `entrega` y `notas`. El orquestador rechaza cualquier salida que no cumpla el esquema.
- **Ningún agente pasa de largo por compliance.** El agente de compliance tiene veto: un `estado: bloqueado` devuelve la pieza al redactor, siempre.
- **La humana decide.** Cada ciclo termina con "Preguntas para Cristina" y nada se publica ni se cierra sin su aprobación explícita.
- **Datos de pacientes: nunca.** Ningún agente recibe datos identificables. Las viñetas clínicas son arquetipos compuestos declarados.
