#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

from sys import stdin

def eje(a,u,v):
    pospol = [0,1] #x,y como si hubiera pasado una unidad de tiempo
    poslad = [a,v] #x,y se inicializa asi para que pueda entrar al ciclo
    x,y = 0,1 #velocidad del policia en x,y para que y pueda avanzar ya que empiezan iguales
    t,timx,timy = 0,0,1 #tiempo total,tiempo x, tiempo y en uno porque ya avanzo
    if a != 0:#evita que entre si empiezan en la misma posicion
        while pospol[0] < poslad[0] or pospol[1] < poslad[1]:
            #parte x
            if pospol[0] < poslad[0]:
                timx += 1
                poslad[0] += u
                x += 1
                pospol[0] += x 
            #parte y
            if pospol[1] < poslad[1]:
                timy += 1
                poslad[1] += v
                y += 1
                pospol[1] += y
        t = max(timx,timy) 
    return t

#10 4 7

def imprimir():
    entrada = stdin.readline()
    #f = open("catch.txt","w")
    while entrada != "":
        a,u,v = entrada.split()
        print(eje(int(a),int(u),int(v)))#, file = f)
        entrada = stdin.readline()
    #f.close()

imprimir()