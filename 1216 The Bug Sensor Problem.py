#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

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