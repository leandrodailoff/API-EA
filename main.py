"""
Cliente para la API de EA Sports FC 26 Pro Clubs.

Este script consume la API no oficial de Pro Clubs para buscar clubes,
obtener sus detalles y ver sus partidos recientes.
"""

import sys

import pandas as pd

from fc26_api_class import FC26_API


def mostrar_resultado(titulo: str, df: pd.DataFrame | None) -> None:
    """Muestra un DataFrame con formato legible."""
    print(f"\n=== {titulo} ===")
    if df is None:
        print("Error en la solicitud.")
    elif df.empty:
        print("No se encontraron resultados.")
    else:
        print(df.to_string())


def buscar_club(api: FC26_API, nombre: str) -> pd.DataFrame | None:
    """Busca un club por nombre, probando variaciones si es necesario."""
    # Intentar con el nombre exacto
    club = api.search_club_by_name(nombre)
    if club is not None and not club.empty:
        return club

    # Si no encuentra, probar con la primera palabra
    primera_palabra = nombre.split()[0] if " " in nombre else nombre
    if primera_palabra != nombre:
        print(f"  No se encontró '{nombre}', probando con '{primera_palabra}'...")
        club = api.search_club_by_name(primera_palabra)
        if club is not None and not club.empty:
            return club

    return club


def main() -> None:
    """Punto de entrada principal."""
    api = FC26_API()

    # Buscar club por nombre
    nombre_club = input("Ingresá el nombre del club a buscar: ").strip()
    if not nombre_club:
        print("Debés ingresar un nombre de club.")
        sys.exit(1)

    club = buscar_club(api, nombre_club)
    if club is None:
        print("Error al buscar el club:", api._last_error)
        sys.exit(1)
    if club.empty:
        print(f"\nNo se encontró ningún club con el nombre '{nombre_club}'.")
        print("\nNota: La API de Pro Clubs solo encuentra clubes que han jugado")
        print("partidos de liga. Si tu club solo jugó amistosos, no aparecerá.")
        print("También verificá que el nombre sea exacto (incluyendo espacios).")
        sys.exit(1)

    # Mostrar resultados de búsqueda
    print(f"\n=== Resultados de búsqueda para '{nombre_club}' ===")
    columnas_mostrar = [c for c in ["clubName", "clubId", "wins", "losses", "ties", "points"] if c in club.columns]
    print(club[columnas_mostrar].to_string(index=False))

    # Si hay múltiples resultados, dejar que el usuario elija
    if len(club) > 1:
        print("\nSe encontraron varios clubes. Usando el primero...")

    club_id = club["clubId"].iat[0]
    nombre = club["clubName"].iat[0]
    print(f"\nClub seleccionado: {nombre} (ID: {club_id})")

    # Obtener detalles del club
    detalles = api.get_club_details(club_id)
    mostrar_resultado("Detalles del club", detalles)

    # Obtener partidos de liga
    partidos = api.get_club_matches_normalized(club_id, "leagueMatch")
    mostrar_resultado("Últimos partidos de liga", partidos)


if __name__ == "__main__":
    main()