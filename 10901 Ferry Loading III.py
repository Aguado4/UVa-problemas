#Juan José Aguado
#Código 8957833
#Fecha 8-02-2023

# Task Description
"""
Before bridges were common, ferries were used to transport cars across rivers. River ferries, unlike their larger cousins, run
on a guide line and are powered by the river’s current. Cars drive onto the ferry from one end, the ferry crosses the river,
and the cars exit from the other end of the ferry.
There is a ferry across the river that can take n cars across the river in t minutes and return in t minutes. A car may arrive at
either river bank to be transported by the ferry to the opposite bank. The ferry travels continuously back and forth between
the banks so long it is carrying a car or there is at least one car waiting at either bank. Whenever the ferry arrives at one
of the banks it unloads its cargo and loads up to n cars that are waiting to cross. If there are more than n, those that have
been waiting the longest are loaded. If there are no cars waiting on either bank, the ferry waits until one arrives, loads it
(if it arrives on the same bank of the ferry), and crosses the river. At what time does each car reach the other side of the
river?
"""

# Input
"""
The first line of input contains c, the number of test cases. Each test case begins with n, t, m. Then m lines follow, each
giving the arrival time for a car (in minutes since the beginning of the day), and the bank at which the car arrives ('left' or
'right').
"""

# Output
"""
For each test case, output one line per car, in the same order as the input, giving the time at which that car is unloaded at the
opposite bank. Output an empty line between cases.
You may assume that 0 < n, t, m ≤ 10 000. The arrival times for each test case are strictly
"""

from heapq import heappush, heapify, heappop
from collections import deque

def eje():
    ent = [int(x) for x in input().split()]
    cap = ent[0] #capacidad del ferry
    tiempo = ent [1] #tiempo que se demora en cruzar
    cant = ent[2] #cantidad de carros que hay
    heapIzq = []
    heapDer = []
    res = deque() #van a haber carros por izquierda y derecha y el resultado
    for i in range(cant):
        ent = input().split()
        if ent[1] == "left":
            heappush(heapIzq, (int(ent[0]),i)) #lo agrego a la lista de la izquierda con su indice
        elif ent[1] == "right":
            heappush(heapDer, (int(ent[0]),i)) #lo agrego a la lista de la derecha con su indice
        res.append(0) #añado a la lista para asi luego poder reemplazar con indices
    viaje = 0 #tiempo que se han demorado
    ferry = "left"
    while len(heapDer) or len(heapIzq):
        viaje += tiempo
        avanza = False
        if len(heapDer) > 0 and heapDer[0][0] <= viaje:
            avanza = True
        if len(heapIzq) > 0 and heapIzq[0][0] <= viaje:
            avanza = True
        if avanza:
            if ferry == "left":
                ferry = "right"
                if len(heapIzq) > 0:
                    for i in range(min(cap, len(heapIzq))):
                        if heapIzq[0][0] <= viaje - tiempo: #si ya ha llegado a la orilla
                            car = heappop(heapIzq)
                            res[car[1]] = viaje
            elif ferry == "right" :
                ferry = "left"
                if viaje != 0 and len(heapDer) > 0:
                    for i in range(min(cap, len(heapDer))):
                        if heapDer[0][0] <= viaje - tiempo: #si ya ha llegado a la orilla
                            car = heappop(heapDer)
                            res[car[1]] = viaje
    return res


def imprimir():
    f = open("ferry.txt", "w")
    casos = int(input()) #recibe el numero de casos
    for i in range(casos): #ejecuta el prigrama para todos los casos
        res = eje() #hace la ejecucion que devuelve una lista
        for j in res:
            print ("%s" %j, file=f) #imprime cada elemento en una linea
        print("", file=f)
    f.close()
imprimir()
