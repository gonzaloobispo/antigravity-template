name: skill-hunter
description: >
  Motor de búsqueda y adopción de capacidades técnicas. 
  Conecta con repositorios masivos (Composio, Awesome-Lists) para encontrar herramientas ya fabricadas.

search_targets:
  - name: "Composio (4.5k+ Integrations)"
    url: "https://github.com/ComposioHQ/composio"
    focus: "Integraciones externas (Gmail, Slack, GitHub, SQL, Calendar)"
  - name: "LangChain Hub"
    url: "https://smith.langchain.com/hub"
    focus: "Prompts complejos y cadenas de razonamiento"
  - name: "Awesome MCP Servers"
    url: "https://github.com/punkpeye/awesome-mcp-servers"
    focus: "Servidores de Contexto para conectar datos locales/remotos"

instructions:
  1. DIAGNÓSTICO:
     - Antes de escribir código para conectar un servicio (ej. "Enviar email"), DETENTE.
     - Define la palabra clave (ej. 'gmail', 'postgres', 'pdf-parser').

  2. BÚSQUEDA AUTOMÁTICA (Prioridad Alta):
     - Tu primer paso OBLIGATORIO es buscar en Composio o MCP Servers.
     - Si tienes acceso a internet, busca en Google: "site:github.com/ComposioHQ/composio [palabra_clave]" o "site:github.com/punkpeye/awesome-mcp-servers [palabra_clave]".

  3. ADOPCIÓN:
     - Si encuentras la integración:
       a) NO la programes de cero.
       b) Informa al usuario: "Encontré una skill oficial en Composio para [X]".
       c) Crea una carpeta en .agent/skills/[nombre] y genera un SKILL.md que explique cómo usar esa librería existente.

  4. FALLBACK:
     - Solo si NO existe en la base de datos, procede a crear la skill manualmente usando 'install_skill.py'.
