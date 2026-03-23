from Herramienta import Herramienta

class Arco(Herramienta):
    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self._flechas = flechas

    @property
    def nombre(self) -> str:
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return "Arco roto, no se puede usar."
        
        if self._flechas <= 0:
            return "Sin flechas"
        
        daño = self.calcular_daño()
        self._flechas -= 1
        self.desgastar()
        return f"Disparando a {objetivo} con daño {daño} (Flechas: {self._flechas})"


# 🚀 PRUEBA tu código
if __name__ == "__main__":
    herramientas = [
        Arco("madera", 1, 0)
    ]
    objetivos = ["Creeper"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()