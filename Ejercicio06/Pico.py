from Herramienta import Herramienta

class Pico(Herramienta):
    """Mina bloques de piedra, carbón, hierro, etc."""
    # TODO: propiedad 'nombre' y método 'usar'
    # En usar(): llama a calcular_daño() y a desgastar()
    pass

    @property
    def nombre(self) -> str:
        return "Pico"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} roto, no se puede usar."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f" Minando {objetivo} con daño {daño}"

    # 🚀 PRUEBA tu código
if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
    ]
    objetivos = ["mena de diamante"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()