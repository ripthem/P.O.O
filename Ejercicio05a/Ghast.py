from Mob import Mob

class Ghast(Mob):

    """Mob Agresivo, "Eaaahgh", Flota y lanza bolas de fuego"""

    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass

    def hacer_sonido(self) -> str:
        return "Eaaahgh"

    def comportamiento(self) -> str:
        return "Agresivo"

    def moverse(self) -> str:
        return "Flota y lanza bolas de fuego"
    
    
    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
       Ghast("Griton", 80),
    ]
    for mob in mobs:
        mob.presentarse()