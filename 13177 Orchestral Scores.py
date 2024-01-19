#Juan José Aguado
#Código 8957833
#Fecha 6-02-2023

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