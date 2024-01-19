#Juan José Aguado
#Código 8957833
#Fecha 7-02-2023

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