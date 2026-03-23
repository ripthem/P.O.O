from Herramienta import Herramienta

class Espada(Herramienta):
    """Ataca mobs causando daño."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} rota, no se puede usar."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f"Atacando a {objetivo} con daño {daño}"




    # 🚀 PRUEBA tu código
if __name__ == "__main__":
    herramientas = [
        Espada("hierro", 3),
    ]
    objetivos = ["Creeper"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()