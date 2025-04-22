# Uso:
# 1. Ejecutar el script.
# 2. Seleccionar un archivo .txt con las declaraciones cuando aparezca la ventana.
# 3. El script mostrará los resultados en la terminal.

# Autores:
#   Luis Fernando Rodríguez Retama   208047
#   Mauricia Peña López Ostolaza     205688
#   Axel Castro Lara                 204092
#   Rafael Harry Gomar Dawson        208999
#   Emilio González Acosta           207911

### IMPORTACIÓN DE PAQUETES ###
import re  # Para manejo de expresiones regulares
import tkinter as tk  # Para la GUI
from tkinter import filedialog  # Para la selección de archivos
from collections import (
    defaultdict,
)  # Para evitar KeyErrors al contar operadores lógicos


### carga_archivo: función para cargar el archivo a evaluar ###
def carga_archivo():
    """
    Abre un diálogo para seleccionar un archivo .txt y retorna su contenido como cadena.

    Returns:
        str | None: El contenido del archivo si fue seleccionado y leído correctamente,
                    o None en caso de error o si no se seleccionó archivo.
    """

    ventana = tk.Tk()  # creamos la ventana principal de la "aplicación" para la UI
    ventana.withdraw()  # no queremos enseñar la ventana, sólo el diálogo que pide el archivo
    path_archivo = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )  # abre el diálogo para archivo .txt y lo asigna a un path
    if path_archivo:  # si el usuario seleccionó un archivo
        try:
            with open(
                path_archivo, "r"
            ) as archivo:  # abre el archivo seleccionado para leerlo (r)
                contenido = archivo.read()  # lee el archivo
                return contenido  # la función regresa el contenido
        except Exception as e:
            print(
                f" ERROR: Fallo en la lectura del archivo: {e}"
            )  # manejamos erres potenciales al seleccionar el archivo
            return None  # la función regresa None
    else:  # el usuario no seleccionó el archivo
        print(
            "ERROR: No se seleccionó un archivo."
        )  # Imprimimos en la consola que no hay archivo para analizar
        return None  # la función regresa None


### tokenizar: separa la cadena identificando un patrón regular ###
def tokenizar(cadena: str) -> list:
    """
    Divide una cadena en tokens utilizando expresiones regulares.

    Args:
        cadena (str): Cadena a analizar.

    Returns:
        list: Lista de tokens encontrados (palabras clave, paréntesis, llaves, etc.).
    """

    # primero se limpian los espacios
    cadena = re.sub(r"\s+", "", cadena)
    # separa buscando 'while's, paréntesis y llaves
    tokens = re.split(r"(while|[{(})])", cadena)
    # desecha tokens vacíos
    tokens = [t for t in tokens if re.match(r".+", t)]
    return tokens


### parseWhiles: revisa anidación de whiles con un autómata de pila ###
def parseWhiles(tokens: list) -> tuple[int, list]:
    """
    Valida la estructura de ciclos while usando un autómata de pila.

    Args:
        tokens (list): Lista de tokens generados a partir de la entrada.

    Returns:
        tuple:
            int: Número de bloques while encontrados correctamente anidados (-1 si hay error).
            list: Lista de expresiones lógicas encontradas en las condiciones de los while.
    """

    contWhiles = 0  # para contar el número de whiles
    expLogicas = []  # para guardar lo que deberían ser comparaciones lógicas
    # el autómata de pila es de un solo estado y aceptará por pila vacía
    pila = ["."]
    for t in tokens:
        p = pila.pop()
        # si t = 'while' y p es '.' o 'x', entonces se introduce un 'p1' a la pila
        if re.match(r"while", t) and re.match(r"\.|x", p):
            pila.append(p)
            pila.append("1")
        # si ( t , p ) = ( '(' , '1' ), entonces se introduce un '2' a la pila
        elif re.match(r"\(", t) and re.match(r"1", p):
            pila.append("2")
        # si p = '2' , t será una expresión lógica (se revisa después) e ingresamos '3' a la pila
        elif re.match(r"2", p):
            pila.append("3")
            expLogicas.append(t)
        # si ( t , p ) = ( ')' , '3' ), entonces se introduce un '4' a la pila
        elif re.match(r"\)", t) and re.match(r"3", p):
            pila.append("4")
        # si ( t , p ) = ( '{' , '4' ), entonces se introduce un '5' a la pila
        elif re.match(r"{", t) and re.match(r"4", p):
            pila.append("x")
        # si ( t , p ) = ( '}' , 'x' ), entonces no se introduce nada
        elif re.match(r"}", t) and re.match(r"x", p):
            contWhiles += 1
        # si ( t , p ) = ( 'while' , 'x'), entonces se introduce 'x1' a la pila
        elif re.match(r"while", t) and re.match(r"x", p):
            pila.append("x")
            pila.append("1")
        # en cualquier otro caso, se tendrán entradas no válidas
        else:
            return (-1, [])
    # simular la transición epsilon
    pila.pop()
    # corroborar aceptación
    if len(pila) != 0:
        contWhiles = -1
    return (contWhiles, expLogicas)


### validar: hace la evaluación completa llamando a parseWhiles y corroborando las comparaciones ###
def validar(cadena) -> bool:
    """
    Ejecuta el análisis sintáctico y semántico sobre una cadena de código fuente.

    Verifica si las estructuras while están bien formadas y si las expresiones lógicas
    dentro de ellas son válidas. Muestra estadísticas sobre variables y operadores.

    Args:
        cadena (str): Código fuente a analizar.

    Returns:
        bool: True si el código es válido, False si hay errores de sintaxis o lógica.
    """

    # tokenización
    tokens = tokenizar(cadena)
    # parseo del autómata de pila y obtención de enunciados lógicos a revisar
    numWhiles, comparaciones = parseWhiles(tokens)
    # revisar si el autómata de pila detectó un error
    if numWhiles < 0:
        print("ERROR: Estructuras while incorrectas")
        return False
    # contenedores para las métricas
    variables = set()
    comparadores = defaultdict(int)
    # expresión regular para revisar los enunciados lógicos
    expLogicas = re.compile(r"([a-zA-Z0-9])(<|>|<=|>=|==|!=)([a-zA-Z0-9])")
    # validación de cada enunciado lógico
    for cad in comparaciones:
        validar = expLogicas.fullmatch(cad)
        # si un enunciado lógico no está bien escrito, se termina el proceso
        if not validar:
            print("ERROR: Comparaciones lógicas incorrectas")
            return False
        grupos = validar.groups()
        # contar el comparador lógico usado
        comparadores[grupos[1]] += 1
        # guardar la(s) variable(s) usadas en la comparación
        for j in [0, 2]:
            if re.match(r"[a-zA-Z]", grupos[j]):
                variables.add(grupos[j])
    # impresión de resultados
    print(f"Número de while's declarados: {numWhiles}")
    print(f"\nNúmero total de variables usadas: {len(variables)}")
    print("\nVariables utilizadas en las expresiones lógicas:")
    print("\t" + " ".join(sorted(variables)))
    print("\nConteo de comparadores lógicos usados:")
    for comp, veces in comparadores.items():
        print(f"\t{comp}\t{veces}")
    return True


### EJECUCIÓN PRINCIPAL###

contenido = carga_archivo()
validar(contenido)

