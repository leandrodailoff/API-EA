# Buenas Prácticas y Git

## Repositorio personal
- Todos los proyectos se suben al repositorio personal de GitHub: **https://github.com/leandrodailoff**
- Antes de commitear/pushear, **siempre verificar** si el repositorio remoto ya existe en GitHub.
- Si el repositorio no existe o hay dudas sobre cuál es el correcto, **preguntar al usuario** antes de crearlo o elegirlo.
- Nunca asumir el repositorio remoto: confirmar siempre con el usuario.

## Commits
- **Todos los mensajes de commit van en español.**
- Usar mensajes claros y descriptivos que expliquen QUÉ se hizo y POR QUÉ.
- Preferir commits atómicos: un commit por cambio lógico.

## Manejo de Git (proyecto personal)
- Es un proyecto **personal** — el usuario es el único que toca el código.
- **No se requieren** flujos estrictos de Git (como Git Flow, PRs, code review).
- Crear **ramas solo para cambios muy grandes** o experimentales.
- Para cambios normales, se puede trabajar directamente en `main`/`master`.
- Mantener el historial limpio y comprensible.

## Estándares generales de código
- Seguir las buenas prácticas del lenguaje/framework en uso.
- Código legible y mantenable por sobre código "inteligente" u optimizado prematuramente.
- Manejo de errores explícito: no silenciar excepciones sin justificación.
- No dejar código muerto, comentarios obsoletos o dependencias sin usar.
- Documentar lo que no sea obvio, pero evitar comentarios redundantes.