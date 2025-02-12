#Juan José Aguado
#Código 8957833
#Fecha 6-02-2023

# Task Description
"""
In a modest orchestra, a big part of the budget goes when buying scores. If each musician had their own copy, the number
could go over 100.
Fortunately, musicians that are playing the same instrument can sit together and share a music stand. That’s a major saving,
but if it is used too much, it can provoke an ugly effect in the concert hall. After all, seeing a lot of musicians in a crowd
behind a stand is not very esthetic.
The section of economic affairs of the orchestra has informed us of the number of scores we can buy for the next concert.
Keeping in mind the number of musicians that play each of the instruments, which stand will be the most concurred?
For example, if we have 8 violins, 5 violas, 5 cellos, and 2 contrabasses and there is enough budget for 6 scores, we can buy
two stands for violins, two for violas, one for cellos and a final one for contrabasses. In this case, the most crowded stand
will be the one from the cellos, with 5 musicians behind it.
"""

# Input
"""
Input will have several test cases, each of them composed by two lines. The first line contains two integers, p and n, with the
number of scores we are allowed to buy (up to 200 000) and the number of different instruments that are part of the orchestra
(up to 100 000). It is guaranteed that it will be possible to buy at least one stand for each type of instrument.
The second line contains n positive numbers indicating the amount of musicians that are part of the orchestra for each of
the instruments (up to 1 000).
"""

# Output
"""
For each test case, write a single integer indicating the number of musicians that will share the most crowded stand, always
meeting the orchestra and budget restrictions. Don’t forget that the objective is to minimize the amount of people in the
most crowded stand.
"""

from heapq import heappush, heapify, heappop
from sys import stdin
import math

def eje(partituras, lista):
    partituras -= len(lista)#las partituras "extra"
    cola = [(mus, mus, 1) for mus in lista] #creo una lista de tuplas con el numero de musicos y el tamaño del atril y el divisor/numero
    #partituras
    heapify(cola) #la organizo
    for i in range(partituras): #se repite por las partituras extra, si no hay no se hace
        tam, orig, div = heappop(cola) #se saca el atril con mas personas
        div += 1
        heappush(cola, ((math.floor(orig/div)), orig, div))#el nuevo valor que se metera
    stand =  int(-1*cola[0][0])#retorna el mayor en positivo
    return stand
 
def imprimir():
    f = open("boxes.txt", "w")
    entrada = stdin.readline() #se recibe la entrada completa
    while (entrada != ""):#se ejecuta hasta que se de la señal de terminar
        part = int(entrada.split()[0])#numero de partituras
        num = [-int(x) for x in input().split()] #volvemos a enteros negativos para tenerlos ordenados por orden descendiente
        print(eje(part,num),file=f)
        entrada = stdin.readline() #se recibe la entrada completa
imprimir()
