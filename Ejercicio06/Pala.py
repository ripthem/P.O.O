from Herramienta import Herramienta

class Pala(Herramienta):
    """Excava tierra, arena y grava rápidamente."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    @property
    def nombre(self) -> str:
        return "Pala"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} rota, no se puede usar."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f"Excavando {objetivo} con eficiencia {daño}"
    
    # 🚀 PRUEBA tu código
if __name__ == "__main__":
    herramientas = [
        Pala("madera", 2),
    ]
    objetivos = ["arena"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()