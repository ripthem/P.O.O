from Jugador import Jugador

class Observador(Jugador):
    """Gana puntos por ver partidas."""
    
    def __init__(self, nombre: str, num_control: str, nivel: str):
        super().__init__(nombre, num_control, nivel)
        self.partidas_vistas = 0

    def ver_partida(self):
        self.partidas_vistas += 1
        print(f"\n{self.nombre} ha visto una partida (Total: {self.partidas_vistas}).")
        self.ganar_puntos(10)

    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Rol: Observador")
        print(f"Partidas Vistas: {self.partidas_vistas}")