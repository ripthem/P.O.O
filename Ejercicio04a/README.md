🍽️ Sistema de Menú de Restaurante (POO)
Este proyecto implementa un sistema de gestión de platillos utilizando Herencia Avanzada en Python. A diferencia de ejemplos básicos, aquí se utiliza el método super() para extender las funcionalidades de la clase padre de manera eficiente.

🧠 Conceptos Clave
Clase Base (Platillo): Define la estructura común para cualquier elemento del menú (nombre y precio).

Herencia con super(): Las clases hijas llaman al constructor del padre para inicializar los atributos comunes, permitiendo que el código sea más limpio y escalable.

Especialización: Cada clase hija (Comida, Bebida, Postre) añade un atributo específico que no existe en las demás.

Polimorfismo: El método tipo() se redefine en cada clase para imprimir detalles específicos según la categoría del elemento.

🏗️ Jerarquía del Menú
Clase	Atributos Heredados	Atributo Específico	Descripción
Platillo	nombre, precio	-	Clase base general.
Comida	nombre, precio	categoria	Ej: Principal, Entrada, Guarnición.
Bebida	nombre, precio	temperatura	indica si es Fría, Caliente o Tiempo.
Postre	nombre, precio	es_sin_gluten (Booleano).
