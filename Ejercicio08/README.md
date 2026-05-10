# 🎮 Torneo de Videojuegos - Instituto Tecnológico de Ensenada

Este proyecto es una práctica de **Programación Orientada a Objetos (POO)** que modela un sistema de registro para el primer torneo de videojuegos del campus. El objetivo principal es aplicar conceptos de **Herencia** y **Polimorfismo** utilizando Python.

## 📋 Descripción del Problema
El sistema permite gestionar dos tipos de participantes:
1. **Competidores**: Jugadores activos que pertenecen a un equipo específico.
2. **Observadores**: Asistentes que acumulan puntos por cada partida que visualizan.

## 📐 Estructura de Clases
- **Jugador (Base)**: Maneja nombre, número de control, nivel y puntos.
- **Competidor**: Añade gestión de equipos y extiende el perfil.
- **Observador**: Añade contador de partidas vistas y lógica de puntos automáticos.
