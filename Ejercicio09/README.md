# 📂 Práctica: Manipulación de Archivos y Cálculo de Tamaño

Este proyecto contiene scripts de Python diseñados para demostrar el manejo básico de archivos de texto (`.txt`) y cómo calcular su peso en diferentes unidades de medida (Bytes, KB y MB).

## 🚀 Funcionalidades

El código realiza tres operaciones principales:

### 1. Creación y Escritura Inicial
Se crea un archivo llamado `test.txt` utilizando el modo de apertura `"w"` (write). 
- Se asegura la codificación `UTF-8`.
- Escribe el saludo inicial: `"hola David"`.

### 2. Anexado Masivo de Datos (Stress Test)
Se reabre el archivo en modo `"a"` (append) para no sobrescribir el contenido previo.
- Utiliza un ciclo `for` para escribir **1,048,576** caracteres ("a").
- Esto permite generar un archivo con un peso suficiente para observar cambios en las unidades de medida.

### 3. Medición del Archivo
Utilizando el módulo `os`, el script recupera el tamaño del archivo y realiza las siguientes conversiones:
- **Kilobytes (Kb):** Tamaño en bytes dividido entre $1024$.
- **Megabytes (Mb):** Tamaño en bytes dividido entre $1024^2$.

## 📊 Ejemplo de Salida en Consola
```text
El tamaño del archivo es: 1024.01 Kb
El tamaño del archivo es: 1.0000 Mb
