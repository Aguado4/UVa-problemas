#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

from sys import stdin
from collections import deque

def eje(n,p1,p2,hue,mem):
    if n in mem: ans = mem[n]
    else:
        if n == len(hue): ans = 0
        else:
            pn1,pn2 = n,n
            while pn1 < len(hue)-1 and hue[pn1+1] <= hue[n]+p1:
                pn1 += 1 
            while pn2 < len(hue)-1 and hue[pn2+1] <= hue[n]+p2:
                pn2 += 1 
            ansp1 = eje(pn1+1,p1,p2,hue,mem) + p1
            ansp2 = eje(pn2+1,p1,p2,hue,mem) + p2
            ans = min(ansp1,ansp2)
        mem[n] = ans
    return ans

def cic(c,p1,p2,hue):
    min = float('inf')
    hue = [x-hue[0] for x in hue]
    if len(hue) > 1:
        for i in range(len(hue)):
            mem = dict()
            res = eje(0,p1,p2,hue,mem)
            if res < min: min = res
            hue = deque(x-hue[1] for x in hue)
            hue.append(hue.popleft()+c) 
    else:
        mem = dict()
        min = eje(0,p1,p2,hue,mem)
    return int(min)


def imprimir():
    #f = open("patches.txt","w")
    entrada = stdin.readline()
    while entrada != "":
        entrada = entrada.split()
        n,c = entrada[0],int(entrada[1]) #numero de huecos,circunferencia de la llanta
        p1,p2 = int(entrada[2]), int(entrada[3]) #parches
        hue = [int(x) for x in input().split()] #coordenadas de los huecos
        print(cic(c,p1,p2,hue))#,file=f)
        entrada = stdin.readline()
    #f.close()
imprimir()