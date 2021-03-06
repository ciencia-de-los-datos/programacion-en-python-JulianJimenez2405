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
    with open("data.csv", "r") as file:
        lista_datos = file.readlines()    

    suma = 0

    for valores in lista_datos:
        valores_temporales = valores.split()
        suma += int(valores_temporales[1])

    return suma


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
    from operator import itemgetter
    from string import whitespace

    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
    data = [row[0] for row in data]

    result=dict()
    for letra in data:
        if letra in result.keys():
            result[letra]=result[letra] + 1
        else:
            result[letra] = 1

    tuplas=[(key,valor) for key, valor in result.items()]
    tuplas=sorted(tuplas,key=itemgetter(0),reverse=False)
    return tuplas


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    diccionario={}
    for i in data:
        if i[0] not in list(diccionario.keys()):
            diccionario[i[0]]=int(i[1]) #key=valor
        elif i[0] in list(diccionario.keys()):
           diccionario[i[0]]+=int(i[1])
    return sorted(list(diccionario.items()))


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
    from collections import Counter
    import csv
    with open('data.csv', 'r', newline='') as data:
        data_reader=csv.reader(data, delimiter='\t')
        list_data=list(data_reader)
        lista=[]
        length=len(list_data)
        for i in range(length):
            lista.append(list_data[i][2][5:7])
    return(sorted(Counter(lista).most_common(len(lista))))


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
    from operator import itemgetter
    with open('data.csv', 'r') as data:
        data_reader=data.readlines()
        data_reader=[row.split('\t') for row in data_reader]
        data_reader=[row[:2] for row in data_reader]
    
        diccionario={}
        for letra, valor in data_reader:
            valor=int(valor)
            if letra in diccionario.keys():
                diccionario[letra].append(valor)
            else:
                diccionario [letra] = [valor]
            
        diccionario = [(key, max(valor), min(valor)) for key, valor in diccionario.items()]
        diccionario = sorted(diccionario, key=itemgetter(0), reverse=False)
    return(diccionario)


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
    import csv
    datos = open('data.csv')
    csvreader=csv.reader(datos)
    lista_1=[]
    lista_2=[]
    lista_3=[]
    lista_4=[]
    lista_5=[]
    for row in csvreader:
        lista_1.append(row[2:])
    for valores in lista_1:
        for data in valores:
            lista_2.append(data.split("\t"))
    for valores in lista_2:
        for data in valores:
            if len(data)>1:
                if data[:3] not in lista_3:
                    lista_3.append(data[:3])
    for data in lista_3:
        numeros=[]
        for valores in lista_2:
            for datos in valores:
                if data in datos:
                    numeros.append(int(datos[4:]))
        lista_4.append(max(numeros))
        lista_5.append(min(numeros))
        tupla=sorted(zip(lista_3,lista_5,lista_4))
    return(tupla)


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    letras=([z[0] for z in data])
    num=list(set([z[1] for z in data]))
    num.sort()
    numyletra=[]
    for n in num:
        lista=[]
        for element in data:
            if element[1] == n:
                lista.append(element[0])
        tupla=(int(n),(lista))
        numyletra=numyletra+[tupla]
    return(numyletra)


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    dic=dict()
    for i in data:
        if int(i[1]) not in dic.keys():
            dic[int(i[1])]=[i[0]]
        else:
            dic[int(i[1])].append(i[0])
        
    result = sorted(list(dic.items()))
    result = [(j[0], sorted(set(j[1]))) for j in result]
    return(result)


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    columna=[(z[4].split(',')) for z in data]
    lista=[]
    for key in range(0, len(columna)):
        for element in range(0, len(columna[key])):
            lista.append([(columna[key][element][:3])])
    claves=list(set([z[0] for z in lista]))
    claves.sort()
    dic={}
    for clave2 in claves:
        contador=0
        for par in lista:
            if par[0] == clave2:
                contador=contador+1
        diccionario={clave2:contador}
        dic.update(diccionario)
    return(dic)


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    result=[]
    for elemento in data:
        result.append((elemento[0],len(elemento[3].split(',')),len(elemento[4].split(','))))
    return(result)


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    columna2=[z[3].split(',') for z in data]
    pares=[]
    for clave in columna2:
        pares=pares+clave
    claves=list(set(pares))
    claves.sort()
    columna=[(z[3].split(','),z[1]) for z in data]
    diccionario={}
    for clave in claves:
        suma=0
        for element in columna:
            for letra in element[0]:
                if letra == clave:
                    suma=suma+int(element[1])
        dic={clave:suma}
        diccionario.update(dic)
    return(diccionario)
    return


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
    with open("data.csv", "r") as data:
        data=open('data.csv', 'r').readlines()
        data=[i.replace('\n', '') for i in data]
        data=[i.split('\t') for i in data]

    letras=list(set([z[0] for z in data]))
    letras.sort()
    columna=[(z[0],sum([int(x[4:]) for x in z[4].split(',')])) for z in data]
    diccionario={}
    for letra in letras:
        suma=0
        for element in columna:
            if element[0] == letra:
                suma=suma+element[1]
        dic={letra:suma}
        diccionario.update(dic)
    return(diccionario)
