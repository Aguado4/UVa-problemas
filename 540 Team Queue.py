#Juan José Aguado
#Código 8957833
#Fecha 3-02-2023

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