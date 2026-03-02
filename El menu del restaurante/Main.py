from Comida import Comida
from Bebida import Bebida
from Postre import Postre

comida1 = Comida("Torta de asada", 90.0,"Principal")
bebida1 = Bebida("CocaCola", 35.0,"Fria")
postre1 = Postre("Carlota", 45.0, False)

comida1.mostrar_info()
comida1.tipo()
print("...")

bebida1.mostrar_info()
bebida1.tipo()
print ("...")

postre1.mostrar_info()
postre1.tipo()