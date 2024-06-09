#Juan José Aguado
#Código 8957833
#Fecha 6-02-2023

from heapq import heappush, heapify, heappop
from sys import stdin
import math

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
