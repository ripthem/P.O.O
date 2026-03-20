from Mob import Mob

class Enderman(Mob):

    """Mob neutral, sonido distorsionado, se teletransporta"""

    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass

    def hacer_sonido(self) -> str:
        return "Sonido distorsionado"

    def comportamiento(self) -> str:
        return "Neutral"

    def moverse(self) -> str:
        return "Se teletransporta"
    


    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Enderman("Tall Boi", 90),
    ]
    for mob in mobs:
        mob.presentarse()