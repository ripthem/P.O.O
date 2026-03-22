⚔️ Sistema de Aventureros RPG (POO)
Este repositorio contiene una implementación de un sistema de clases de personajes para un juego de rol, utilizando Programación Orientada a Objetos en Python. El enfoque principal es demostrar cómo diferentes tipos de personajes pueden compartir una base común pero ejecutar acciones únicas.

🧬 Arquitectura del Código
El sistema utiliza una estructura de Clase Padre y Clases Hijas especializadas:

1. Clase Base: Aventurero
Es el molde general para todos los personajes.

Atributos: nombre y nivel.

Métodos: presentarse(): Acción común para todos los héroes.
usar_habilidad(): Un método que será definido por cada profesión.

2. Clases Especializadas (Herencia)
Cada clase hereda de Aventurero y añade su propio equipamiento o recursos:

🛡️ Guerrero: Añade el atributo arma. Su habilidad consiste en un ataque físico directo.
🔮 Mago: Añade el atributo hechizo. Su habilidad permite lanzar magia específica.
🏹 Arquero: Añade un sistema de gestión de recursos (flechas). Su habilidad tiene una validación lógica: si no tiene flechas, no puede atacar.

🚀 Conceptos de Programación Aplicados
Uso de super(): Se utiliza para llamar al constructor de la clase padre, asegurando que el nombre y el nivel se asignen correctamente antes de añadir los atributos únicos de clase.
Polimorfismo: El método usar_habilidad() se comporta de forma distinta según el objeto que lo llame (un Guerrero ataca, un Mago lanza hechizos, un Arquero dispara).
Lógica de Control: El Arquero incluye una estructura condicional (if/else) dentro de su método para manejar el inventario de flechas.
