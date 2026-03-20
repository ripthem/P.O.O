from Mob import Mob

class Aldeano(Mob):

    """Mob pasivo, suena 'hnh', camina por la aldea."""

    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass

    def hacer_sonido(self) -> str:
        return "Hnh"

    def comportamiento(self) -> str:
        return "Pasivo"

    def moverse(self) -> str:
        return "Camina por la aldea"
    
    
    # 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Aldeano("Jose", 35),
    ]
    for mob in mobs:
        mob.presentarse()