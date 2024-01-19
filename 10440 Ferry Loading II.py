#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

from math import ceil

def eje(n,t,c):
    cant, act, cont = len(c), 0, n - 1
    if cant % n == 0:
        while cont < cant:
            if cont != cant - 1: act = max(act,c[cont]) + 2 * t
            else: act = max(act,c[cont]) + t 
            cont += n
        ans = (act,max(cant/n,1))
    else:
        cont = (cant % n) - 1
        act = c[cont] + 2 * t
        cont += n
        while cont < cant:
            if cont != cant - 1: act = max(act,c[cont]) + 2 * t
            else: act = max(act,c[cont]) + t
            cont += n
        ans = (act, ceil(cant/n))
    return ans

def imprimir():
    #f = open("fer.txt","w")
    numcas = int(input())
    for i in range(numcas):
        n,t,m = input().split()
        c = []
        for j in range(int(m)):
            c.append(int(input()))
        c.sort()
        if int(n) >= int(m): res = (c[-1] + int(t),1)
        else:res = eje(int(n),int(t),c)
        print("%d %d"%(res[0],res[1]))#,file = f)
    #f.close()
imprimir()