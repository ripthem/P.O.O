👾 Minecraft Mob System: Abstracción Aplicada
Este proyecto implementa un sistema de entidades (Mobs) utilizando Clases Abstractas de Base (ABC) en Python. El objetivo es estandarizar el comportamiento de diferentes criaturas del juego, asegurando que todas compartan una estructura mínima pero mantengan su identidad única.

🧠 ¿Qué aprendemos con este código?
Este ejercicio demuestra la diferencia entre métodos abstractos y métodos concretos dentro de una misma clase:
Métodos Abstractos: La clase Mob obliga a todas las subclases a definir hacer_sonido(), comportamiento() y moverse(). Si una criatura no define esto, el juego no sabría cómo procesarla.
Método Concreto: El método presentarse() es igual para todos. No necesitamos escribir el código de impresión en cada clase hija; el padre sabe cómo mostrar los datos de cualquier Mob.

🏗️ Jerarquía de Entidades
Clase Base: Mob
Define los atributos básicos: nombre y vida. Además, establece la interfaz de comunicación.

Clases Implementadas
Cada clase hija representa un ente con mecánicas distintas:
Criatura
Sonido
Comportamiento
Movimiento
🐄 Vaca"Muuuu", Pasivo, Camina lento
🧨 Creeper "...Ssssss", Agresivo, Corre hacia el jugador
🌌 Enderman "Distorsionado", Neutral, Se teletransporta
👨‍🌾 Aldeano "Hnh", Pasivo, Camina por la aldea
👻 Ghast "Eaaahgh", Agresivo, Flota y lanza fuego
