###
## Excepciones basicas

#Parte 1: try / except simple
print("=" * 50)
print("PARTE 1: Division con manejo de erroes")
print("=" * 50)

try:
    a = (input("Ingresa el numerador: "))
    b = (input("Ingresa el denominador: "))
    total= a / b

except ValueError:
    print("Error: Debes ingresar un numero entero no una letra o simbolo.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# Parte 2: try / except con else
else:
    print(f"El resultado de {a} / {b} es: {total} ")

finally:
    print("Gracias por usar el programa de division!")
