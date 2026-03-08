class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad
    # Aumento de felicidad en 10 puntos (max 100)
    def alimentar(self):
        self.nivelFelicidad += 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100
    # Aumento de felicidad en 20 (max 100)
    def jugar(self):
        self.nivelFelicidad += 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100
            
    #Mostrar estado actual
    def mostrarEstado(self):
        return f"{self.nombre} de tipo {self.tipo} con nivel de felicidad: {self.nivelFelicidad}"
    # Nivel de felicidad
    def esFeliz(self):
        return self.nivelFelicidad > 70


# Crear mascota1
mascota1 = Mascota("Stella", "Gato", 1, 50)
#Interaccion con mascota
print(mascota1.mostrarEstado())
print(f"¿Es feliz? {mascota1.esFeliz()}")
 
mascota1.alimentar()
print(mascota1.mostrarEstado())

mascota1.jugar()
print(mascota1.mostrarEstado())
print(f"¿Es feliz? {mascota1.esFeliz()}")

# Crear mascota2
mascota2 = Mascota("Spike", "Perro",2, 10)
#Interaccion con mascota
print(mascota2.mostrarEstado())
print(f"¿Es feliz? {mascota2.esFeliz()}")
 
mascota2.alimentar()
print(mascota2.mostrarEstado())

mascota2.jugar()
print(mascota2.mostrarEstado())
print(f"¿Es feliz? {mascota2.esFeliz()}")


