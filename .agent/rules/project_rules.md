# Guía Maestra de Arquitectura Agéntica: Google Antigravity v4.0

## 1. Filosofía: El Paradigma "Agent-First"
En Antigravity, tu rol evoluciona de "escritor de código" a **Orquestador**. Usted define el *qué*; los agentes resuelven el *cómo*.
1. **Mínima Intervención:** Si requiere >3 clics, delégalo.
2. **Confianza por Verificación:** Exige videos (Artifacts) del agente probando la app.
3. **Proactividad:** El agente debe proponer mejoras y detectar deuda técnica.

## 2. Protocolo de Investigación (Regla de Oro)
**Obligatorio:** Antes de codificar, investiga el ecosistema (GitHub/Docs) para usar el estado del arte (2025/2026). Actualiza .agent/rules/tech-stack.md.

## 3. Estándares de Ingeniería (Hard Rules)
Detecta el entorno (package.json, pyproject.toml) y usa scripts locales.
* **JS/TS:** npm run build/test. Variables camelCase.
* **Python:** poetry/ruff/pytest. Variables snake_case. Tipado estricto obligatorio.
* **General:** No loguear secretos. Tests deterministas y descriptivos.

## 4. Ingeniería de "Skills" y Modo Loki
* **Skills:** Usar estructura .agent/skills/ (SKILL.md + scripts/).
* **Modo Loki:** Para tareas complejas, actúa como Gerente de Producto: desglosa requisitos y despacha sub-agentes en paralelo.

## 5. Automatización Total
1. **TDD Autónomo:** Falla primero, arregla después.
2. **Browser Surface:** Graba video del uso real de la app como evidencia.
3. **Auto-Fix:** Corrige errores autónomamente (hasta 3 intentos).

## 6. Seguridad y Gobernanza
* **Sandbox:** Pide permiso para comandos destructivos (rm, ssh).
* **Auditoría:** Escanea .env en busca de secretos antes de cada commit.

## 7. Contexto de Dominio Dinámico
* **Instrucción Crítica:** Antes de planificar, LEE OBLIGATORIAMENTE los archivos en **.agent/context/**.
* **Nota:** Si la carpeta está vacía, usa el conocimiento general. Si hay archivos, tienen prioridad absoluta.

## 2.1 Protocolo de Adquisición de Skills
* **Busca antes de construir:** Antes de desarrollar una funcionalidad compleja, activa la skill 'skill-hunter' para ver si existe un módulo comunitario o MCP Server que resuelva el problema.

## 2.4 Protocolo de Evolución del Sistema
* **Mantenimiento SOTA:** Una vez por semana (o a petición), ejecuta system-evolver para verificar si nuestra arquitectura sigue siendo puntera. Si encuentras algo mejor en internet, propón una actualización inmediata.
