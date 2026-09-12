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


def main() -> None:
    """Punto de entrada principal."""
    api = FC26_API()

    # Buscar club por nombre
    nombre_club = input("Ingresá el nombre del club a buscar: ").strip()
    if not nombre_club:
        print("Debés ingresar un nombre de club.")
        sys.exit(1)

    club = api.search_club_by_name(nombre_club)
    if club is None:
        print("Error al buscar el club:", api._last_error)
        sys.exit(1)
    if club.empty:
        print(f"No se encontró ningún club con el nombre '{nombre_club}'.")
        sys.exit(1)

    club_id = club["clubId"].iat[0]
    print(f"\nClub encontrado: {club['name'].iat[0]} (ID: {club_id})")

    # Obtener detalles del club
    detalles = api.get_club_details(club_id)
    mostrar_resultado("Detalles del club", detalles)

    # Obtener partidos de liga
    partidos = api.get_club_matches_normalized(club_id, "leagueMatch")
    mostrar_resultado("Últimos partidos de liga", partidos)


if __name__ == "__main__":
    main()