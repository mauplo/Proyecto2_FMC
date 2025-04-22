# Reconocimiento de enunciados while

## Descripción

Este programa es reconocedor de enunciados while bien formados en Kotlin. Está diseñado para:

- **Identificar bloques while:** Detecta y cuenta bloques while con operadores `<, >, ==, >=, <=, !=`, variables de un caracter `[a-z]` y constantes de un dígito `[0-9]`
- **Clasificar:**
- **Generar estadísticas:**
- **Rechazar bloques inválidos:**

## Características Principales

- **Análisis de bloques:** Verifica y cuenta los bloques while que se enuncian en el archivo de entrada.
- **Clasificación:** Separa las variables y operadores usados dentro de los whiles.
- **Interfaz amigable:** Usa una ventana emergente (Tkinter) para seleccionar el archivo de entrada.
- **Manejo de errores:** Rechaza entradas no válidas. Incorpora control de excepciones durante la lectura del archivo.

## Requisitos

- **Python 3.x:** Se recomienda Python 3.6 o superior.
- **Tkinter:** Este módulo, utilizado para la interfaz gráfica, viene generalmente incluido en la instalación estándar de Python.
- **Librerías estándar:** `re` y `collections` (no se requiere instalación adicional).

## Instalación

1. **Verifica Python:** Asegúrate de tener Python 3 instalado.
2. **Comprueba Tkinter:** Ejecuta el siguiente comando para confirmar que Tkinter está disponible:
    ```bash
    python -m tkinter
    ```
    Si se abre una ventana de prueba, Tkinter está correctamente instalado.
3. **Descarga el código:** Clona o descarga el repositorio que contiene el programa.

## Cómo Ejecutarlo

1. **Abre la terminal:** Navega hasta el directorio donde se encuentra el archivo del programa (por ejemplo, `clasificador.py`).
2. **Ejecuta el programa:** Ingresa el siguiente comando en la terminal:
    ```bash
    python clasificador.py
    ```
3. **Selecciona el archivo:** Al iniciarse, se abrirá una ventana emergente solicitando seleccionar un archivo de texto (`.txt`) que contenga los datos de entrada (conjunto de bloques while sintácticamente correctos).
4. **Observa el resultado:** Una vez analizado el archivo, el programa mostrará en la terminal un resumen con:
    - Numero total de variables (diferentes) usadas en todos los while encontrados.
    - Numero total de operadores de comparación encontrados (con repeticiones).
    - Numero total de while's que contienen los bloques parseados.

## Ejemplos de Ejecución

### Ejemplo 1
**Prueba válida:**

**Entrada Kotlin:**
```kotlin
```
**Salida:**
```
```

## Problemas Conocidos
- **Limitación de tipos**:
- **Alcance de las declaraciones**:

## Detalles Técnicos y Modularización
- **Expresiones Regulares**:
Se utilizan expresiones regulares complejas para capturar los enunciados de while, tanto para operaciones con variables y constantes. Esto permite identificar correctamente el tipo de dato (constante o variable).

- **Interfaz Gráfica con Tkinter**:
La función `carga_archivo()` utiliza Tkinter para abrir una ventana emergente que permite seleccionar el archivo de texto a analizar.

- **Manejo de Errores**:
Se han implementado bloques `try/except` para gestionar posibles errores durante la lectura del archivo, asegurando que el programa informe adecuadamente al usuario en caso de problemas.

- **Modularización**:
El código está organizado en funciones específicas:
    - `carga_archivo()`: Gestiona la selección y lectura del archivo.
    - `tokenizar`: separa la cadena identificando un patrón regular.
    - `parseWhiles`: revisa anidación de whiles con un autómata de pila.
    - `validar`: hace la evaluación completa llamando a parseWhiles y corroborando las comparaciones.

## Consideraciones Finales
- **Formato del archivo**:
El programa espera archivos de texto (.txt) con bloques while en formato Kotlin. Asegúrate de que el contenido respete la sintaxis básica para obtener estadísticas correctas.

- **Ejecución en diferentes entornos**:
Dado que se utiliza Tkinter para la selección de archivos, el programa está optimizado para entornos de escritorio.

- **Ampliación del análisis**:
Actualmente, el programa se enfoca en bloques de while relativamente simples. Para proyectos más complejos, se podrían implementar mejoras para reconocer y guardar el nombre de variables más largos y constantes más grandes. 

# Autores 
- Axel Castro Lara – 204092
- Mauricia Peña López Ostolaza – 205688
- Emilio González Acosta – 207911
- Luis Fernando Rodríguez Retama – 208047
- Rafael Harry Gomar Dawson – 208999
