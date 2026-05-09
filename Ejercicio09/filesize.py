import os 
ruta = "test.txt"
# Medida en bytes 
size = os.path.getsize(ruta)
Kb = size / 1024
Mb = size / (1024 ** 2)
print(f"El tamaño del archivo es: {Kb:.2f} Kb")
print(f"El tamaño del archivo es: {Mb:.4f} Mb")