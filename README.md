# API-EA

Cliente en Python para la **API no oficial de EA Sports FC 26 Pro Clubs**.

Este proyecto consume la API de Pro Clubs para buscar clubes, obtener sus detalles y ver sus partidos recientes. La API es pública y no requiere autenticación.

## Requisitos

- Python 3.9+
- Dependencias en [`requirements.txt`](requirements.txt)

## Instalación

1. Crear el ambiente virtual:
   ```bash
   py -m venv .venv
   ```

2. Activar el ambiente virtual:
   ```bash
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

```bash
python main.py
```

El script te pedirá el nombre de un club, lo buscará, mostrará sus detalles y sus últimos partidos de liga.

## Estructura del proyecto

```
├── main.py               → Script principal (CLI interactiva)
├── fc26_api_class.py     → Cliente de la API (descargado de fc26-clubs-api)
├── requirements.txt      → Dependencias
└── .clinerules/          → Reglas de Cline
```

## API

La API base es `https://proclubs.ea.com/api/fc` y los endpoints disponibles son:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `search_club_by_name(nombre)` | `allTimeLeaderboard/search` | Busca un club por nombre |
| `get_club_details(club_id)` | `clubs/info` | Obtiene detalles de un club |
| `get_club_matches(club_id, tipo)` | `clubs/matches` | Obtiene partidos de un club |
| `get_club_matches_normalized(club_id, tipo)` | `clubs/matches` | Partidos normalizados |

Tipos de partido válidos: `friendlyMatch`, `leagueMatch`, `playoffMatch`.

## Nota

Esta es una API **no oficial** y no está afiliada ni respaldada por EA. Los endpoints pueden cambiar o desaparecer sin aviso.