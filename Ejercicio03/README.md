Ejercicio: Herencia y Polimorfismo (Animales)
Este proyecto demuestra cómo reutilizar código mediante la jerarquía de clases en Python. Se implementa una clase base (padre) y varias clases derivadas (hijas) que heredan sus atributos y modifican su comportamiento.

🧬 Conceptos Aplicados
Herencia: Las clases Perro y Gato heredan los atributos nombre y edad de la clase Animal, evitando la duplicación de código.

Polimorfismo (Sobrescritura de Métodos): Aunque todos los animales pueden "hablar", cada especie lo hace de forma distinta. Hemos redefinido el método hablar() en cada clase hija para que emita el sonido correspondiente.

Modularización: El código está preparado para ser dividido en diferentes archivos (Animal.py, Perro.py, Gato.py), facilitando el mantenimiento.

🏗️ Estructura de Clases
Clase Padre: Animal
Es la base de la jerarquía. Define las propiedades comunes de cualquier animal:

Atributos: nombre, edad.

Métodos: 
describir(): Imprime la presentación básica del animal.
hablar(): Un método genérico que por defecto no emite sonidos específicos (...).

Clases Hijas: Perro y Gato
Heredan todo de Animal pero personalizan su comunicación:

Perro: Al llamar a hablar(), imprime un "Guau!".
Gato: Al llamar a hablar(), imprime un "Miau!".
