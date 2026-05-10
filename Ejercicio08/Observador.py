from Jugador import Jugador

class Observador(Jugador):
    """Gana puntos por ver partidas."""
    
class Observador(Jugador):
    def __init__(self, nombre, num_control, nivel):
        super().__init__(nombre, num_control, nivel)
        self.partidas_vistas = 0 

    def ver_partida(self):
        self.partidas_vistas += 1
        self.ganar_puntos(5)

    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Rol: Observador")
        print(f"Partidas Vistas: {self.partidas_vistas}")