import random  # Importamos el módulo random para decidir en caso de empate

# Función para jugar un partido entre dos equipos
def jugar_partido(equipo1, equipo2):
    print(f"{equipo1} vs {equipo2}")  # Imprime el enfrentamiento
    gol1 = int(input(f"Ingrese goles de {equipo1}: "))  # Solicita los goles del primer equipo
    gol2 = int(input(f"Ingrese goles de {equipo2}: "))  # Solicita los goles del segundo equipo
    if gol1 > gol2:
        return equipo1  # Gana el equipo 1 si tiene más goles
    elif gol2 > gol1:
        return equipo2  # Gana el equipo 2 si tiene más goles
    else:
        print("Empate! Se decide por penales...")
        return equipo1 if random.choice([True, False]) else equipo2  # En caso de empate, se elige aleatoriamente un ganador

# Función para jugar una ronda del torneo
def jugar_ronda(partidos, ronda):
    print(f"\n{ronda}")  # Imprime el nombre de la ronda
    ganadores = []  # Lista para almacenar los ganadores
    for clave, (equipo1, equipo2) in partidos.items():
        ganador = jugar_partido(equipo1, equipo2)  # Se juega el partido
        ganadores.append(ganador)  # Se guarda el ganador
        print(f"Ganador: {ganador}\n")  # Muestra el ganador del partido
    return ganadores  # Devuelve la lista de ganadores

# Función principal del torneo
def torneo():
    # Diccionario con los enfrentamientos de octavos de final
    octavos = {
        "4.1": ("Países Bajos", "Estados Unidos"),
        "4.2": ("Argentina", "Australia"),
        "4.3": ("Francia", "Polonia"),
        "4.4": ("Inglaterra", "Senegal"),
        "4.5": ("Japón", "Croacia"),
        "4.6": ("Brasil", "Corea del Sur"),
        "4.7": ("Marruecos", "España"),
        "4.8": ("Portugal", "Suiza")
    }
    
    # Se juegan los octavos de final y se obtienen los equipos clasificados a cuartos
    cuartos_equipos = jugar_ronda(octavos, "Cuartos de Final")
    cuartos = {f"Q{i+1}": (cuartos_equipos[i], cuartos_equipos[i+1]) for i in range(0, len(cuartos_equipos), 2)}
    
    # Se juegan los cuartos de final y se obtienen los equipos clasificados a semifinales
    semifinales_equipos = jugar_ronda(cuartos, "Semifinales")
    semifinales = {f"S{i+1}": (semifinales_equipos[i], semifinales_equipos[i+1]) for i in range(0, len(semifinales_equipos), 2)}
    
    # Se juegan las semifinales y se obtienen los finalistas
    final_equipos = jugar_ronda(semifinales, "Final")
    
    # Se juega el partido por el tercer puesto
    tercer_puesto = jugar_partido(semifinales_equipos[0], semifinales_equipos[1])
    
    # Se imprimen los resultados finales del torneo
    print("\nResultados Finales:")
    print(f"Campeón: {final_equipos[0]} 🏆")
    print(f"Subcampeón: {final_equipos[1]}")
    print(f"Tercer lugar: {tercer_puesto}")

# Iniciar el torneo
torneo()
