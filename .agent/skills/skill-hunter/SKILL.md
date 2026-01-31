name: skill-hunter
description: >
  Activa esta skill cuando necesites una nueva capacidad técnica (ej. 'conectar a SQL', 'analizar PDFs', 'manejar AWS') 
  y quieras buscar si ya existe una solución prefabricada en la comunidad o en GitHub antes de escribirla desde cero.

instructions:
  1. ANALIZAR: Define claramente qué capacidad falta (ej. "Necesito un MCP Server para PostgreSQL").
  2. BUSCAR:
     - Usa tus herramientas de navegación para buscar en GitHub topics como 'mcp-server', 'agent-skill' o 'cursor-rules'.
     - Busca en repositorios de confianza de la comunidad (ej. 'punkpeye/awesome-mcp-servers').
  3. EVALUAR:
     - Verifica que la skill encontrada tenga licencia compatible (MIT/Apache).
     - Revisa si tiene documentación clara.
  4. INSTALAR:
     - Si encuentras una skill útil, usa el script 'install_skill.py' para clonarla o crear la estructura en '.agent/skills/'.
     - ADAPTA el archivo SKILL.md descargado al formato v4.0 de este proyecto.
