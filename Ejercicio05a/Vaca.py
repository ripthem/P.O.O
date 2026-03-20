from Mob import Mob

class Vaca(Mob):

    """Mob pasivo, suena 'muuuu', camina lento."""

    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass

    def hacer_sonido(self) -> str:
        return "Muuuu"

    def comportamiento(self) -> str:
        return "Pasivo"

    def moverse(self) -> str:
        return "Camina lento"
    
    
    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 20),
    ]
    for mob in mobs:
        mob.presentarse()