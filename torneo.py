import random

def jugar_partido(equipo1, equipo2):
    print(f"{equipo1} vs {equipo2}")
    gol1 = int(input(f"Ingrese goles de {equipo1}: "))
    gol2 = int(input(f"Ingrese goles de {equipo2}: "))
    if gol1 > gol2:
        return equipo1
    elif gol2 > gol1:
        return equipo2
    else:
        print("Empate! Se decide por penales...")
        return equipo1 if random.choice([True, False]) else equipo2

def jugar_ronda(equipos, ronda):
    print(f"\n{ronda}")
    ganadores = []
    for i in range(0, len(equipos), 2):
        ganador = jugar_partido(equipos[i], equipos[i+1])
        ganadores.append(ganador)
        print(f"Ganador: {ganador}\n")
    return ganadores

def torneo():
    equipos = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4", 
               "Equipo 5", "Equipo 6", "Equipo 7", "Equipo 8", 
               "Equipo 9", "Equipo 10", "Equipo 11", "Equipo 12", 
               "Equipo 13", "Equipo 14", "Equipo 15", "Equipo 16"]
    
    octavos = jugar_ronda(equipos, "Octavos de Final")
    cuartos = jugar_ronda(octavos, "Cuartos de Final")
    semifinales = jugar_ronda(cuartos, "Semifinales")
    finalistas = jugar_ronda(semifinales, "Final")
    
    print(f"El campeón del torneo es: {finalistas[0]} 🏆")

torneo()
