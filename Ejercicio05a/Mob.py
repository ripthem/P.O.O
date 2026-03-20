# Importa el módulo para clases abstractas
from abc import ABC, abstractmethod

class Mob(ABC):
    """Clase abstracta base para todos los mobs."""

    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida

    # Métodos ABSTRACTOS: cada mob DEBE implementarlos

    @abstractmethod
    def hacer_sonido(self) -> str:
        """Retorna el sonido característico del mob."""
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        """Retorna 'pasivo' o 'agresivo'."""
        pass

    @abstractmethod
    def moverse(self) -> str:
        """Describe cómo se mueve el mob."""
        pass

    # Método CONCRETO: igual para todos los mobs

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"❤️  Vida       : {self.vida} HP")
        print(f"🔊  Sonido     : {self.hacer_sonido()}")
        print(f"⚔️  Tipo       : {self.comportamiento()}")
        print(f"🏃  Movimiento : {self.moverse()}")
        print()

    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Mob("test", 10)
    ]
    for mob in mobs:
        mob.presentarse()
# Exception has occurred: TypeError
# Can't instantiate abstract class Mob without an implementation for abstract methods 'comportamiento', 'hacer_sonido', 'moverse'
# No deja hacerlo directo, ya que la clase 'Mob' funciona como clase abstracta, para que funcione debo importar "from Mob immport Mob" y crear una subclase 'Mob'.
