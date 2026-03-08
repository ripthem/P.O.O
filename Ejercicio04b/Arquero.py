from Aventurero import Aventurero

class Arquero(Aventurero):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre, nivel)
        self.flechas = flechas

    def usar_habilidad(self):
        if self.flechas > 0:
            self.flechas -= 1
            print(f"{self.nombre} dispara una flecha! Le quedan {self.flechas}. 🏹")
        else:
            print(f"{self.nombre} no quedan flechas")