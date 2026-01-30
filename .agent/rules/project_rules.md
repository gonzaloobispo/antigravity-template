Aquí tienes la **Guía Maestra de Arquitectura y Desarrollo en Google Antigravity (v3.0)**.  
Esta versión es la más completa hasta la fecha. Integra la nueva arquitectura de **"Skills" comunitarias** (como el modo Loki), establece protocolos de **seguridad crítica** (debido a vulnerabilidades recientes detectadas), prioriza la **investigación en tiempo real** para evitar la obsolescencia tecnológica y detalla el marco teórico físico para tu aplicación de propulsión.

# Guía Maestra de Arquitectura Agéntica: Google Antigravity v3.0

## 1\. Filosofía: El Arquitecto en la Era del "Agent-First"

Google Antigravity no es un editor de texto con esteroides; es una plataforma de **orquestación de fuerza laboral digital**. Tu rol cambia de escribir sintaxis a dirigir un equipo de agentes autónomos que planifican, codifican, prueban y despliegan,.

### Principios de Operación

1. **Hiper-Automatización:** El objetivo es reducir tu intervención manual a cero. Si una tarea requiere más de tres clics, debe delegarse a un agente,.  
2. **Confianza por Verificación (Artifacts):** Nunca confíes en un "listo". Exige **Artefactos**: planes de implementación, *diffs* de código y, crucialmente, **grabaciones de video** del agente probando la app en el navegador,.  
3. **Proactividad Extrema:** El agente no solo espera órdenes; debe proponer mejoras de arquitectura, detectar deuda técnica y sugerir *features* basándose en su análisis del contexto del proyecto,.

## 2\. Protocolo de Investigación y Actualización (Obligatorio)

**⚠️ REGLA CRÍTICA:** El ecosistema de IA cambia semanalmente. Antes de iniciar cualquier tarea técnica, el agente debe actualizar su conocimiento. No asumas que las librerías de ayer son las mejores de hoy.

### El Flujo de "Investigación Primero"

Instruye a tu chatbot arquitecto para que ejecute este ciclo antes de generar código:

* **Reconocimiento en Tiempo Real:**  
* *Instrucción:* "Antes de codificar, usa tus herramientas de navegación para investigar el 'Estado del Arte' (SOTA) actual para TECNOLOGÍA/TAREA. Busca en GitHub Trending, Hacker News y documentación oficial."  
* *Objetivo:* Evitar el uso de librerías depreciadas o patrones de diseño obsoletos que el modelo base (con fecha de corte de entrenamiento) podría sugerir,.  
* **Validación de Herramientas:**  
* Si el agente sugiere una librería, ordénale: "Verifica la última versión estable y si existen problemas de seguridad recientes reportados (CVEs)".  
* **Actualización de Contexto:**  
* El agente debe actualizar dinámicamente el archivo .agent/rules/tech-stack.md con los hallazgos para que todos los futuros agentes del proyecto usen el nuevo estándar,.

## 3\. Ingeniería de "Skills": El Cerebro Modular

Las **Skills** son la diferencia entre un chatbot genérico y un ingeniero senior especializado. Son paquetes de archivos que le dan al agente capacidades de ejecución real (acceso a BD, despliegue, auditoría),.

### A. Arquitectura de una Skill

Una Skill reside en .agent/skills/ (local) o \~/.gemini/antigravity/skills/ (global) y se compone de,:

* **SKILL.md (El Detonador):**  
* **Descripción Semántica:** Es vital. El agente escanea esto para saber *cuándo* activarse.  
* *Ejemplo:* "Use this skill when the user asks to audit security vulnerabilities or check for exposed API keys."  
* **Scripts de Ejecución (/scripts):**  
* No dejes que la IA "alucine" comandos. Proporciónale scripts en Python o Bash probados para tareas críticas (ej. migraciones de base de datos, limpieza de logs).  
* **Recursos Estáticos (/resources):**  
* Plantillas de código, encabezados de licencia o guías de estilo que el agente debe inyectar textualmente,.

### B. "Loki Mode": Orquestación Multi-Agente

Basado en los avances de la comunidad, implementa el patrón **"Loki Mode"**. Esto transforma al agente en un **Gerente de Producto** que,:

* Desglosa un PRD (Documento de Requisitos del Producto) vago en tareas técnicas.  
* Despacha **sub-agentes** especializados en paralelo: uno para Frontend, otro para Backend, otro para QA.  
* Utiliza una "Skill de Orquestación" para mantener el estado del proyecto y no perder el contexto en tareas largas.

**Repositorio de Referencia:** Busca integrar el *58-Skill Antigravity Aggregator* para dotar a tu agente de roles predefinidos como "Security Auditor", "Senior Engineer" (TDD) y "Growth Manager",.

## 4\. Desarrollo y Testing Autónomo (El Bucle de Auto-Reparación)

### A. TDD (Test-Driven Development) Autónomo

Configura a tu agente para que opere bajo la lógica: **"Falla primero, arregla después"**,.

1. **Generación de Tests:** "Crea un test unitario que falle para la funcionalidad X".  
2. **Implementación:** "Escribe el código mínimo para pasar el test".  
3. **Refactorización:** "Optimiza el código sin romper el test".

### B. La Superficie del Navegador (Browser Surface)

Antigravity tiene un navegador Chrome integrado que el agente controla. Úsalo para **QA Visual**:

* **Instrucción:** "Abre la app en localhost, regístrate como usuario nuevo, añade un producto al carrito y procede al checkout. Graba un video de todo el proceso".  
* **Validación:** El agente te entregará un video (Artifact) donde verás el cursor moviéndose y escribiendo. Si falla (ej. un botón no responde), el agente capturará el error de consola, leerá el DOM y **se auto-reparará** sin tu ayuda,.

## 5\. Seguridad y Gobernanza (¡Crítico\!)

Investigaciones recientes han detectado vulnerabilidades de **inyección de prompt** y exfiltración de datos en Antigravity,. Como Arquitecto, debes blindar el entorno:

* **Sandbox Estricto:**  
* Configura la política de ejecución de terminal en **"Ask User"** (Preguntar al usuario) para comandos destructivos o de red (curl, rm, ssh),.  
* Nunca abras repositorios de fuentes desconocidas directamente en Antigravity sin auditoría previa; un archivo SKILL.md malicioso podría ejecutar código en tu máquina,.  
* **Skills de Auditoría:**  
* Implementa una Skill de "Security Audit" que escanee automáticamente en busca de claves de API expuestas (.env) antes de cualquier *commit*, ya que los agentes pueden filtrar estos datos accidentalmente en los logs,.

## 6\. Contexto Teórico para tu App: "Pathfinder Mark V-B"

Si tu objetivo es generar la app de simulación física propuesta, utiliza este marco teórico validado en tus fuentes para alimentar la "memoria" del agente arquitecto:

### Física de Propulsión y Métrica del Espacio-Tiempo

* **Concepto Central:** Ingeniería métrica mediante el **Campo de Desplazamiento de Solitones** (Soliton Displacement Field). No usa antimateria, sino deformación geométrica,.  
* **Mecanismo de Activación:** Utiliza **Superradiancia de Vapor de Rubidio**. Pulsos láser de teravatios interactúan con celdas de vapor de Rubidio para crear efectos ópticos no lineales (Efecto Kerr) que alteran el índice de refracción del vacío,.  
* **Energía:** Reactor de **Fusión Aneutrónica de Boro (p-11B)**. Genera partículas alfa cargadas para electricidad directa, sin radiación de neutrones, esencial para la seguridad de la tripulación,.  
* **Navegación "Ricochet":**  
* *Problema:* A velocidades FTL (superlumínicas), no puedes ver lo que hay delante.  
* *Solución:* Algoritmo estocástico que detecta "badenes gravitacionales" (fluctuaciones de masa) y hace que la nave "rebote" o se desvíe en trayectorias no lineales calculadas probabilísticamente,.  
* **Límite de Schwinger:** El sistema opera al borde de este límite ($10^{29} W/cm^2$), donde el campo electromagnético es tan fuerte que "ablanda" el vacío, permitiendo su manipulación,.

**Prompt para el Agente:**  
"Actúa como físico teórico e ingeniero de software. Diseña una simulación en Python/WebGPU que visualice la métrica de Alcubierre modificada por el efecto de Superradiancia. Implementa el algoritmo de navegación 'Ricochet' para que la nave autónoma evite obstáculos gravitacionales en un entorno 3D generado proceduralmente."

## 7\. Resumen del Flujo de Trabajo (Cheat Sheet)

1. **Inicio:** Abre Antigravity \> Agent Manager.  
2. **Prompt de Investigación:** "Investiga las mejores herramientas para X en 2026\. Actualiza stack.md."  
3. **Activación de Skills:** El agente detecta la intención y carga frontend-skill o backend-skill automáticamente.  
4. **Ejecución:** El agente escribe código, crea tests y **abre el navegador** para validar.  
5. **Revisión:** Tú miras el video (Artifact) y el plan. Si es correcto, apruebas.  
6. **Despliegue:** El agente usa una Skill de deployment para subir a Vercel/AWS.


