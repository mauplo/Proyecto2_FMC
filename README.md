# Reconocimiento de enunciados while

## Descripción

El siguiente programa es un reconocedor de enunciados while bien formados en Kotlin. Está diseñado para:

- **Identificar bloques while:** Detecta y cuenta bloques while con operadores `<, >, ==, >=, <=, !=`, variables de un caracter `[a-z]` y constantes de un dígito `[0-9]`
- **Recuperar variables:** Hace un listado de las variables utilizadas en las expresiones lógicas.
- **Generar estadísticas:** Se imprime un conteo de la cantidad de whiles y los comparadores lógicos usados.
- **Bloques inválidos:** Cuando el archivo de texto revisado tiene bloques inválidos, imprime un mensaje de rechazo.

## Características Principales

- **Análisis de bloques:** Verifica y cuenta los bloques while que se enuncian en el archivo de entrada.
- **Clasificación:** Separa las variables y operadores usados dentro de los whiles.
- **Interfaz amigable:** Usa una ventana emergente (Tkinter) para seleccionar el archivo de entrada.
- **Manejo de errores:** Rechaza entradas no válidas. Incorpora control de excepciones durante la lectura del archivo.

## Requisitos

- **Python 3.9:** Se necesita python 3.9 o superior por la sintaxis `tuple[int, list]:`
- **Tkinter:** Este módulo, utilizado para la interfaz gráfica, viene generalmente incluido en la instalación estándar de Python.
- **Librerías estándar:** `re` y `collections` (no se requiere instalación adicional).

## Instalación

1. **Verificar Python:** Ejecutar el siguiente comando para confirmar que Python 3.9 está instalado:
   ```bash
    python --version 
    ```
   (Si no sirve ese comando, intentar: python3 --version)

2. **Compruebar Tkinter:** Ejecutar el siguiente comando para confirmar que Tkinter está disponible:
    ```bash
    python -m tkinter
    ```
    Si se abre una ventana de prueba, Tkinter está correctamente instalado.
3. **Descarga el código:** Clonar o descargar el repositorio que contiene el programa.

## Cómo Ejecutarlo

Una vez descargado el archivo [main.py](main.py) 

1. **Abrir la terminal:** Navegar hasta el directorio donde se encuentra el archivo del programa 
2. **Ejecuta el programa:** Ingresar el siguiente comando en la terminal:
    ```bash
    python main.py
    ```
3. **Selecciona el archivo:** Al iniciarse, se abrirá una ventana emergente solicitando seleccionar un archivo de texto (`.txt`) que contenga los datos de entrada (conjunto de bloques while sintácticamente correctos). Se pueden usar los casos de prueba del repositorio como [prueba_valida.txt](prueba_valida.txt)
4. **Observa el resultado:** Una vez analizado el archivo, el programa mostrará en la terminal un resumen con:
    - Número de total de while's declarados
    - Número total de variables usadas
    - Variables utilizadas en las expresiones lógicas
    - Conteo de comparadores lógicos usados

## Ejemplos de Ejecución

### Ejemplo 1
[prueba_valida.txt](prueba_valida.txt)

**Entrada Kotlin:**
```kotlin
while (x < y) {

    while (4 == 2) {

        while (z > a) {

        }

        while (b == d) {

        }

    }

}

while (x <= z) {

}

while (a > b) {

    while (f != 5) {

    }

}

while (3 >= 2) {}

while (c != d) {
}

while (m <= n) {

}

while (1 < x) {

}

while (y >= 0) {

}

while (g == h) {

}

while (k != 9) {

}
```
**Salida:**
```
Número de while's declarados: 14

Número total de variables usadas: 13

Variables utilizadas en las expresiones lógicas:
        a b c d f g h k m n x y z

Conteo de comparadores lógicos usados:
        <       2
        ==      3
        >       2
        <=      2
        !=      3
        >=      2
```

### Ejemplo 2
[prueba_invalida.txt](prueba_invalida.txt)
Ejemplo donde falta un corchete que se abre en el primer while 

**Entrada Kotlin:**
```kotlin
while (x < y) 

    while (4 == 2) {

        while (z > a) {

        }

        while (b == d) {

        }

    }

}

```

**Salida:**
```
ERROR: Estructuras while incorrectas
```

## Problemas Conocidos
- **Bloques vacíos/simples**: Solo se reconoce sintaxis básica de bloques `while` sin comentarios ni contenido adicional dentro de los bloques.
- **Longitud de variables**: Solo se reconocen variables de un carácter. Identificadores como `total`, `x1`, o `bandera` no son aceptados.
- **Tipos de operadores**: Solo reconoce operadores de comparación básicos `<, >, ==, !=, <=, >=`. Otros operadores lógicos como `&&`, `||` o `!` no están implementados.
- **Errores por línea**: Si hay un error, no se indica la línea exacta donde ocurre, solo se rechaza el texto en general.

## Detalles Técnicos y Modularización
- **Expresiones Regulares**:
Se utilizan expresiones regulares y pilas para capturar los enunciados de while, para diferentes operaciones. Esto permite identificar correctamente el tipo de dato (constante o variable).

- **Interfaz Gráfica con Tkinter**:
La función `carga_archivo()` utiliza Tkinter para abrir una ventana emergente que permite seleccionar el archivo de texto a analizar.

- **Manejo de Errores**:
Se han implementado bloques `try/except` para gestionar posibles errores durante la lectura del archivo, asegurando que el programa informe adecuadamente al usuario en caso de problemas.

- **Modularización**:
El código está organizado en 4 funciones específicas:
    - `carga_archivo()`: Gestiona la selección y lectura del archivo.
    - `tokenizar`: separa la cadena identificando un patrón regular.
    - `parseWhiles`: revisa anidación de whiles con un autómata de pila.
    - `validar`: hace la evaluación completa llamando a parseWhiles y corroborando las comparaciones.

## Consideraciones Finales
- **Formato del archivo**:
El programa espera archivos de texto (.txt) con bloques while en formato Kotlin. Es importante  que el contenido respete la sintaxis básica para obtener estadísticas correctas.

- **Ejecución en diferentes entornos**:
Dado que se utiliza Tkinter para la selección de archivos, el programa está optimizado para entornos de escritorio.

- **Ampliación del análisis**:
Actualmente, el programa se enfoca en bloques de while relativamente simples. Para proyectos más complejos, se podrían implementar mejoras para reconocer y guardar los bloques de while aun cuando el archivo tenga comentarios o instrucciones dentro de las llaves `{}`. Asimismo, sería importante poder recibir nombres de variables más largos y constantes más grandes. 

# Autores 
- Luis Fernando Rodríguez Retama – 208047
- Mauricia Peña López Ostolaza – 205688
- Axel Castro Lara – 204092
- Rafael Harry Gomar Dawson – 208999
- Emilio González Acosta – 207911

