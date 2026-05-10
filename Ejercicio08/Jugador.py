class Jugador:
    """Clase Base que representa a cualquier jugador del torneo."""
    
    def __init__(self, nombre: str, num_control: str, nivel: str):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = 0

    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"¡{self.nombre} ha ganado {cantidad} puntos! Total: {self.puntos}")

    def perder_puntos(self, cantidad: int):
        if self.puntos - cantidad >= 0:
            self.puntos -= cantidad
        else:
            self.puntos = 0
        print(f"{self.nombre} ha perdido {cantidad} puntos. Total: {self.puntos}")

    def mostrar_perfil(self):
        print(f"\n--- Perfil de Jugador ---")
        print(f"Nombre: {self.nombre}")
        print(f"No. Control: {self.num_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos Totales: {self.puntos}")