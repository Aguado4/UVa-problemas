#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
Mr. Macdonald is a farmer. He has a huge land to manage. To monitor the number of bugs in his land, he asks help
from the famous professor T. Professor T is an expert on computer science. Professor T studies several efficient approach
and suggests Mr. Macdonald to setup a wireless sensor system in his land. The system will be setup as follows: in
each predefined location, one wireless sensor will be established. Since all sensors are operated by batteries, the powers
consumed by the sensors are determined by the effective communication distance (ECD) between sensors. Mr. Macdonald
is a nice old man. He prefers not to trouble professor T much. Therefore, he decides that all sensors will be set in the same
power level. That is, all sensors will have the same effective communication distance.
The land is so huge that it is not possible to cover all spots by the sensors. However, each sensor can broadcast the collected
data to their neighbors as long as the neighbors are in its effective communication distance. But the total number of sensors
is relative small comparing to the land. Mr. Macdonald needs to travel the whole land to collect the data from sensors
everyday. Mr. Macdonald is getting old. He hopes that the computer in his house can collect all data from all sensors
automatically. Again, he called professor T for help. This time, professor T suggests Mr. Macdonald to setup a base station
in his house. The house is right in the center of the land.
Due to the limited budget, the number of receiver/transmitter Mr. Macdonald can afford is limited and is relatively small
comparing to the total number of sensors. It is impossible to assign receiver/transmitter to every sensor. Therefore, sensors
with no receiver/transmitter need to send their data to the sensor with receiver/transmitter (directly or indirect) first, After
that, the sensor with receiver/transmitter sends all data it receives from other sensors along with the data it collects back to
the base station. You may assume that the receiver/transmitter has enough power such that it always can send data back to
the base station.
Professor T promises to write the necessary software to make all sensors work together in this way, but one important
issue need to be studied. If all sensors are set at the maximum power level, all sensors might be able to send their data
back without troubles, but the battery will be out-of-power soon. To save power, professor T need to decide the minimum
power level needed such that the battery can have longest operating time while all sensor data can be col- lected by the base
station. Although professor T is good in programming, he is weak in algorithm design. Your goal is to help professor T to
write a program to determine the minimum power level needed to set all sensors accordingly. To simplify our problem,
please report the ECD corresponding to the minimum power level. Please apply the ceiling function to your answer.
Here is an example: assume that the land is 10 × 10. There are three sensors, located at (1, 1), (2, 1), and (8, 7). We also
assume that there are 2 receiver/transmitters. In this example, the ECD of all sensors need to be set at 1.

Input
The first line contains the number of test cases w, 1 ≤ w ≤ 10. Then the w test cases are listed one by one. In each test case,
the first line is a single integer, representing the number of receiver/transmitters for that test case. After that, the test case
consists of some lines with two blank-separated numbers X Y in each line: X is an integer, denoting the x-coordinate of the
sensor, and Y is also an integer, denoting the y-coordinate of the same sensor.
Each test case is ended by the following line: ‘-1’. Please note that the land is a rectangle with dimemsions 10 0000 ×
10 0000.

Output
For each test case, output the corresponding ECD.
"""

import math as m

def findset(v,p):
    if v == p[v]: ans = v
    else:
        p[v] = findset(p[v],p)
        ans = p[v]
    return ans

def union(u,v,p,rango):
    u, v = findset(u,p), findset(v,p)
    if u != v:
        if rango[u] < rango[v]: u,v = v,u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1
    return p,rango

def eje(trans,sensor):
    grafo,rango,p = [],[],[]
    for i in range(len(sensor)):
        rango.append(0)#rango inicializado en 0 para todos los nodos
        p.append(i)#el padre de cada nodo comienza siendo si mismo
        for j in range(i+1,len(sensor)):#se agregan las conexiones a todos los demas nodos por distancia euclidiana
            grafo.append((m.sqrt((sensor[i][0] - sensor[j][0])**2 + (sensor[i][1]-sensor[j][1])**2),i,j))
    grafo.sort()#se ordena y comenzamos con la conexion mas barata
    mst,i = [],0#minimal spanning tree
    while len(mst) != len(sensor) - (trans): #hacemos el mst hasta que tengamos todas las conexiones menos los transmisores
        peso, u, v = grafo[i]#peso y los dos nodos que conectan
        if findset(u,p) != findset(v,p):#si estan en conjuntos distintos
            mst.append(grafo[i])#se agrega la conexion al mst ya que no genera ciclos
            p,rango = union(u,v,p,rango)#se unen para que esten en el mismo arbol
        i += 1
    ans = m.ceil(mst[-1][0])
    return ans

def imprimir():
    #f = open("bug.txt","w")
    numcas = int(input())
    for i in range(numcas):
        trans = int(input())
        entrada = input().split()
        sensor = []
        while entrada[0] != "-1":
            x,y = entrada[0],entrada[1]
            sensor.append((int(x),int(y)))
            entrada = input().split()
        print(eje(trans,sensor))#,file = f)
    #f.close()

imprimir()
