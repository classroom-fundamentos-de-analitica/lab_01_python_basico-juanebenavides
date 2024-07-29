"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    with open("data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            suma += int(columns[1])
    return suma


#datos_segunda_columna = pregunta_01()
#print(datos_segunda_columna)



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

    # Inicializar un diccionario para contar las ocurrencias de cada letra
    counts = {}
    
    # Abrir el archivo y leer línea por línea
    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (la letra)
            letter = columns[0]
            # Contar la ocurrencia de la letra
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = sorted(counts.items())
    
    return result

#print(pregunta_02())



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
    # Inicializar un diccionario para sumar los valores de la segunda columna por cada letra
    sums = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (la letra)
            letter = columns[0]
            # Obtener el valor de la segunda columna y convertirlo a entero
            value = int(columns[1])
            # Sumar el valor en el diccionario
            if letter in sums:
                sums[letter] += value
            else:
                sums[letter] = value
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = sorted(sums.items())
    
    return result


#print(pregunta_03())


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
    month_counts = {}
    

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la fecha de la tercera columna
            date = columns[2]
            # Extraer el mes de la fecha (YYYY-MM-DD)
            month = date.split('-')[1]
            # Contar la ocurrencia del mes
            if month in month_counts:
                month_counts[month] += 1
            else:
                month_counts[month] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por el mes
    result = sorted(month_counts.items())
    
    return result


#print(pregunta_04())


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
    min_max_values = {}
    
    # Abrir el archivo y leer línea por línea
    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (letra) y la segunda columna (valor)
            letter = columns[0]
            value = int(columns[1])
            # Actualizar los valores máximo y mínimo para la letra
            if letter in min_max_values:
                min_max_values[letter]['max'] = max(min_max_values[letter]['max'], value)
                min_max_values[letter]['min'] = min(min_max_values[letter]['min'], value)
            else:
                min_max_values[letter] = {'max': value, 'min': value}
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = [(letter, values['max'], values['min']) for letter, values in sorted(min_max_values.items())]
    
    return result

#print(pregunta_05())


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
    value_ranges = {}
    
    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la quinta columna (el diccionario codificado)
            encoded_dict = columns[4]
            # Separar las entradas del diccionario
            entries = encoded_dict.split(',')
            for entry in entries:
                key, value = entry.split(':')
                value = int(value)
                if key in value_ranges:
                    value_ranges[key]['min'] = min(value_ranges[key]['min'], value)
                    value_ranges[key]['max'] = max(value_ranges[key]['max'], value)
                else:
                    value_ranges[key] = {'min': value, 'max': value}
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la clave
    result = [(key, values['min'], values['max']) for key, values in sorted(value_ranges.items())]
    
    return result

#print(pregunta_06())



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
    # Inicializar un diccionario para almacenar las listas de letras por valor de la columna 2
    associations = {}
    
    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener el valor de la columna 2 y la letra de la columna 1
            value = int(columns[1])
            letter = columns[0]
            # Agregar la letra a la lista correspondiente en el diccionario
            if value in associations:
                associations[value].append(letter)
            else:
                associations[value] = [letter]
    
    # Convertir el diccionario en una lista de tuplas y ordenar por el valor de la columna 2
    result = sorted(associations.items())
    
    return result

#print(pregunta_07())


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
    # Inicializar un diccionario para almacenar las letras únicas por valor de la columna 2
    associations = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener el valor de la columna 2 y las letras de la columna 1
            value = int(columns[1])
            letters = columns[0]
            # Agregar las letras a la lista correspondiente en el diccionario
            if value in associations:
                associations[value].update(letters)
            else:
                associations[value] = set(letters)
    
    # Convertir el diccionario en una lista de tuplas y ordenar por el valor de la columna 2
    result = [(key, sorted(list(letters))) for key, letters in sorted(associations.items())]
    
    return result

#print(pregunta_08())


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
    counts = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la columna 5 y dividirla en claves y valores
            if len(columns) > 4:  # Asegurarse de que la columna 5 existe
                entries = columns[4].split(',')
                for entry in entries:
                    key = entry.split(':')[0]
                    # Contar cada clave
                    if key in counts:
                        counts[key] += 1
                    else:
                        counts[key] = 1

    result = [key for key in sorted(counts.items())]
    result = dict(result)
    return result


#print(pregunta_09())


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
    # Inicializar una lista para almacenar los resultados
    result = []

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            if len(columns) > 4:
                letter = columns[0]
                col4_count = len(columns[3].split(','))
                col5_count = len(columns[4].split(','))
                result.append((letter, col4_count, col5_count))
    
    return result


#print(pregunta_10())


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
    sums = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            if len(columns) > 4:
                value = int(columns[1])
                letters = columns[3].split(',')
                
                for letter in letters:
                    # Sumar los valores en la columna 2 para cada letra de la columna 4
                    if letter in sums:
                        sums[letter] += value
                    else:
                        sums[letter] = value
    
    # Ordenar el diccionario por las claves (letras) alfabéticamente
    sorted_sums = dict(sorted(sums.items()))
    
    return sorted_sums


#print(pregunta_11())


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
    # Inicializar un diccionario para almacenar la suma de los valores de la columna 5 por letra en la columna 1
    sums = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            if len(columns) > 4:
                letter = columns[0]
                # Dividir la columna 5 en entradas
                entries = columns[4].split(',')
                # Sumar los valores en la columna 5
                total_sum = sum(int(entry.split(':')[1]) for entry in entries)
                
                # Sumar al total acumulado para la letra correspondiente
                if letter in sums:
                    sums[letter] += total_sum
                else:
                    sums[letter] = total_sum
    result = [letter for letter in sorted(sums.items())]
    result = dict(result)
    return result

# Llamar a la función y mostrar el resultado
#print(pregunta_12())