from Comida import Comida
from Bebida import Bebida
from Postre import Postre

comida1 = Comida("Tacos de asada", 40.0,"Principal")
bebida1 = Bebida("CocaCola", 40.0,"Fria")
postre1 = Postre("Carlota", 60.0, True)

comida1.mostrar_info()
comida1.tipo()
print("---")

bebida1.mostrar_info()
bebida1.tipo()
print ("---")

postre1.mostrar_info()
postre1.tipo()
