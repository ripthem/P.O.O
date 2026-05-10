from Jugador import Jugador
from Competidor import Competidor 
from Observador import Observador

if __name__ == "__main__":
    print("TORNEO TEC")
    
    # Competidor
    jugador = Competidor("David Castro", "25760822", "Avanzado", "Reappers")
    jugador.ganar_puntos(70)
    jugador.mostrar_perfil()
    
    print("-" * 10)
    
    # Observador
    espectador = Observador("Johana Aguilera", "22758334", "Intermedio")
    espectador.ver_partida()
    espectador.mostrar_perfil()