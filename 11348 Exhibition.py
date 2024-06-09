#Juan José Aguado
#Código 8957833
#Fecha 7-02-2023

# Task Description
"""
Some friends have the same hobby, they are collecting stamps. Once upon a time they decided to make an exhibition.
Exhibition brought them some money and now they do not know how to divide their income. They decided to divide their
money according this rule: “The percent of whole income that i-th friend will get is equal to the part of his unique stamp’s
type.”
The stamp type is called unique if and only if this type of stamps of owned only by one person.

Input
The first line contains integer K (0 < K ≤ 100), it is number of tests. Each test case is described by positive integer N
(0 < N ≤ 50), it’s the number of friends. Next goes N lines with integers. Each line corresponds one friend stamp collection.
The first integer on the line is M — the number of stamps owned by a person (0 < M ≤ 50). Next goes M integers A
(0 ≤ A ≤ 10 000) — types of stams.

Output
For each test case out line formatter like this: ’Case i : a1%a2%a3% . . . an%’. Where i is a test number, and ai percent of
income that goes to i-th friend.
"""


def eje():
    amigos = int(input())#leemos el numero de amigos
    uniAm = [] #lista con el numero de unicos en los indices de los equipos
    unicas = 0 #contador de unicos
    dicEst = {}#diccionario estamp:equipos en los que esta
    for i in range(amigos):#hacemos una lista de estampillas por cada amigo
        entrada = input().split()#recibimos el numero de estampillas con las estampillas
        listEst = set() #se crea el set por amigo
        for j in range(1, int(entrada[0]) + 1, 1): #se guardan las estampillas
            listEst.add(entrada[j]) #se añade la estampilla al set del amigo
            if entrada[j] in dicEst: #si ya esta esa estampilla en el diccionario 
                dicEst[entrada[j]].add(i)#se añade el equipo al que pertenece
            else:
                dicEst[entrada[j]] = {i} #si no, se crea un set y se añade al equipo en el que esta
        uniAm.append(len(listEst)) #asumo que todas las que se agregaron son unicas
        unicas += len(listEst) #sumo todas las estampillas del amigo
    for i in dicEst:
        if len(dicEst[i]) > 1:
            unicas -= len(dicEst[i])
            for j in dicEst[i]:
                uniAm[j] -=1
    if unicas > 0:
        for i in range(0, len(uniAm), 1):
            uniAm[i] = (uniAm[i] / unicas) * 100 
    else:
        for i in range(0, len(uniAm), 1):
            uniAm[i] = 0
    return uniAm

def imprimir():
    casos = int(input())
    for i in range(1, casos + 1): #hacemos el numero de casos que nos digan
        salida = "Case %s:"%i
        res = eje()
        for j in (res):
            salida += " " + "%s"%f'{j:.6f}' + "%"
        print(salida)
imprimir()
