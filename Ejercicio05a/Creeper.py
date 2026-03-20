from Mob import Mob

class Creeper(Mob):

    """Mob agresivo, suena '...Ssssss', corre hacia el jugador"""

    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass

    def hacer_sonido(self) -> str:
        return "...Ssssss"

    def comportamiento(self) -> str:
        return "Agresivo"

    def moverse(self) -> str:
        return "Corre hacia el jugador"


    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Creeper("Explosi", 50),
    ]
    for mob in mobs:
        mob.presentarse()