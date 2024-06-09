#Juan José Aguado
#Código 8957833
#Fecha 3-02-2023

# Task Description
"""
Queues and Priority Queues are data structures which are known to most computer scientists. The Team Queue, however, is
not so well known, though it occurs often in everyday life. At lunch time the queue in front of the Mensa is a team queue,
for example.
In a team queue each element belongs to a team. If an element enters the queue, it first searches the queue from head to tail
to check if some of its teammates (elements of the same team) are already in the queue. If yes, it enters the queue right
behind them. If not, it enters the queue at the tail and becomes the new last element (bad luck). Dequeuing is done like in
normal queues: elements are processed from head to tail in the order they appear in the team queue.
Your task is to write a program that simulates such a team queue.
"""

# Input
"""
The input file will contain one or more test cases. Each test case begins with the number of teams t (1 ≤ t ≤ 1 000). Then t
team descriptions follow, each one consisting of the number of elements belonging to the team and the elements themselves.
Elements are integers in the range 0..999 999. A team may consist of up to 1000 elements.
Finally, a list of commands follows. There are three different kinds of commands:
• ENQUEUE x — enter element x into the team queue
• DEQUEUE — process the first element and remove it from the queue
• STOP — end of test case
The input will be terminated by a value of 0 for t.
Warning: A test case may contain up to 200 000 (two hundred thousand) commands, so the implementation of the team
queue should be efficient: both enqueing and dequeuing of an element should only take constant time.
"""

# Output
"""
For each test case, first print a line saying ‘Scenario #k’, where k is the number of the test case. Then, for each ‘DEQUEUE’
command, print the element which is dequeued on a single line. Print a blank line after each test case, even after the last
one.
"""

from collections import deque 

def eje(equipos):
    tempCola = deque() #se hace una lista enlazada para los indices de los equipos
    dicEqui = {} #diccionario donde la llave es el equipo #ind:[miembros]
    res = deque() #se hace una lista enlazada con el resultado (los que hacen dequeue)
    ent = input().split()
    while (ent[0] != "STOP"): #hasta que se pare el proceso
        if (ent[0] == "ENQUEUE"):
            if (dicEqui.get(equipos[ent[1]],"no esta") == "no esta"): #si el equipo no esta en la cola
                dicEqui[equipos[ent[1]]] = deque([ent[1]]) #agrega al dic el equipo con la cola hasta el momento
                tempCola.append(equipos[ent[1]]) #añade el ind del equipo a la cola temporal
            else: #si el equipo esta en la cola
                dicEqui[equipos[ent[1]]].append(ent[1]) #añade el elemento a la derecha de la cola del equipo
        elif ent[0] == "DEQUEUE":
            res.append(dicEqui[tempCola[0]].popleft()) #saca el primer elemento de la cola temporal y 
            #lo agrega al final del resultado
            if (len(dicEqui[tempCola[0]]) == 0): #si no hay mas miembros del equipo en la cola se quita
                dicEqui.pop(tempCola[0])
                tempCola.popleft()
        ent = input().split()
    return res

def imprimir():
    numEquip = int(input()) #se introduce el numeró de equipos
    scenario = 1 #numero de casos que se han hecho
    while (numEquip != 0): #se ejecuta hasta que se de la señal de terminar
        equipos = {} #un diccionario de equipos con llave siendo el elemento y de valor el indice del equipo
        for i in range(0, numEquip, 1): #repite la recolección de entradas por el numero de equipos
            tempequipos = input().split() #entrada completa
            for j in range(1, int(tempequipos[0]) + 1, 1):
                equipos[tempequipos[j]] = i
        res = eje(equipos)
        print("Scenario #%s"%(scenario)) #se imprime el numero del caso
        salida = ""
        for i in range(0, len(res), 1): #se imprime la cola
            salida += str(res[i]) + "\n"
        print(salida)
        scenario += 1 #se le suma uno al caso
        numEquip = int(input()) #se puede acabar el ciclo con 0 o se repite
    
imprimir()
