"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = r'data.csv'
    total = 0
    with open(data) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            total += int(row[1])  # Sumar el valor de la segunda column
    return total


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = r'data.csv'
    conteo_letras = {}

    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = fila[0]
            if primera_letra in conteo_letras:
                conteo_letras[primera_letra] += 1
            else:
                conteo_letras[primera_letra] = 1

    conteo_ordenado = sorted(conteo_letras.items())
    return conteo_ordenado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = r'data.csv'
    conteo_letras = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = fila[0]
            if primera_letra in conteo_letras:
                conteo_letras[primera_letra] += int(fila[1])
            else:
                conteo_letras[primera_letra] = int(fila[1])
    conteo_ordenado = sorted(conteo_letras.items())
    return conteo_ordenado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = r'data.csv'
    conteo_meses = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = fila[2].split("-")
            if primera_letra[1] in conteo_meses:
                conteo_meses[primera_letra[1]] += 1
            else:
                conteo_meses[primera_letra[1]] = 1
    conteo_ordenado = sorted(conteo_meses.items())
    return conteo_ordenado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = r'data.csv'
    max_min_por_letra = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            letra = fila[0][0]
            valor = int(fila[1])
            if letra in max_min_por_letra:
                max_valor, min_valor = max_min_por_letra[letra]
                max_valor = max(max_valor, valor)
                min_valor = min(min_valor, valor)
                max_min_por_letra[letra] = (max_valor, min_valor)
            else:
                max_min_por_letra[letra] = (valor, valor)
    max_min_por_letra_lista = sorted(max_min_por_letra.items())
    l = []
    for letra, (max_valor, min_valor) in max_min_por_letra_lista:
        l.append((letra, max_valor, min_valor))
    return l


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = r'data.csv'
    max_min_por_letra = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            letra = fila[4].split(",")
            for i in range(len(letra)):
                letra1 = letra[i].split(":")
                if letra1[0] in max_min_por_letra:
                    max_valor, min_valor = max_min_por_letra[letra1[0]]
                    max_valor = max(max_valor, int(letra1[1]))
                    min_valor = min(min_valor, int(letra1[1]))
                    max_min_por_letra[letra1[0]] = (max_valor, min_valor)
                else:
                    max_min_por_letra[letra1[0]] = (int(letra1[1]), int(letra1[1]))
    max_min_por_letra_lista = sorted(max_min_por_letra.items())
    l1 = []
    for letra, (max_valor, min_valor) in max_min_por_letra_lista:
        l1.append((letra, min_valor, max_valor))
    return l1


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = r'data.csv'
    conteo_letras = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = int(fila[1])
            if primera_letra in conteo_letras:
                conteo_letras[primera_letra].append(fila[0])
            else:
                conteo_letras[primera_letra] = []
                conteo_letras[primera_letra].append(fila[0])
    conteo_ordenado = sorted(conteo_letras.items())
    return conteo_ordenado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = r'data.csv'
    conteo_letras = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = int(fila[1])
            if primera_letra in conteo_letras:
                if fila[0] not in conteo_letras[primera_letra]:
                    conteo_letras[primera_letra].append(fila[0])
            else:
                conteo_letras[primera_letra] = []
                conteo_letras[primera_letra].append(fila[0])
            conteo_letras[primera_letra].sort()
    conteo_ordenado = sorted(conteo_letras.items())
    return conteo_ordenado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = r'data.csv'
    max_min_por_letra = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            letra = fila[4].split(",")
            for i in range(len(letra)):
                letra1 = letra[i].split(":")
                if letra1[0] in max_min_por_letra:
                    max_min_por_letra[letra1[0]] += 1
                else:
                    max_min_por_letra[letra1[0]] = 1
    max_min_por_letra = {k: max_min_por_letra[k] for k in sorted(max_min_por_letra.keys())}
    return max_min_por_letra


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = r'data.csv'
    max_min_por_letra = []
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            i3 = fila[3].split(",")
            i4 = fila[4].split(",")
            max_min_por_letra.append((fila[0], len(i3), len(i4)))

    return max_min_por_letra


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = r'data.csv'
    conteo_letras = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = int(fila[1])
            x = fila[3].split(",")
            for i in range(len(x)):
                if x[i] in conteo_letras:
                    conteo_letras[x[i]] += primera_letra
                else:
                    conteo_letras[x[i]] = primera_letra
    conteo_letras = {k: conteo_letras[k] for k in sorted(conteo_letras.keys())}
    return conteo_letras


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = r'data.csv'
    conteo_letras = {}
    with open(data, mode='r') as file:
        lector_csv = csv.reader(file, delimiter='\t')
        for fila in lector_csv:
            primera_letra = fila[0]
            x = fila[4].split(",")
            for i in range(len(x)):
                n = x[i].split(":")
                if primera_letra in conteo_letras:
                    conteo_letras[primera_letra] += int(n[1])
                else:
                    conteo_letras[primera_letra] = int(n[1])
    conteo_letras = {k: conteo_letras[k] for k in sorted(conteo_letras.keys())}
    return conteo_letras