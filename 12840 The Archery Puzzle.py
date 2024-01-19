#Juan José Aguado
#Código 8957833
#Fecha 17-04-2023

from collections import deque
opt = None
def eje(tot, points,n,sol):
    global opt
    if not (opt != None and opt != ["impossible"] and len(opt) == 1): #acaba en caso de que solo una flecha basta
        if tot == 0:
            if opt == None or len(sol) < len(opt):
                opt = list(sol)
        else:
            if not (opt != None and opt != ["impossible"] and len(sol)>=len(opt)):
                while n > -1:
                    if tot >= points[n] and (tot - points[n] >= points[0] or tot - points[n] == 0):
                        sol.append(points[n])
                        eje(tot-points[n],points,n,sol)
                        sol.pop()
                    n -= 1
                if sol == [] and opt == None: opt = ["impossible"]
    return opt

def imprimir():
    #f = open("arch.txt","w")
    global opt
    numcas = int(input())
    for i in range(numcas):
        N,S = input().split()
        points = [int(x) for x in input().split()] 
        sol = []
        opt = None
        res = deque(map(str,eje(int(S),points,len(points)-1,sol)))
        if res[0] != "impossible": res.extendleft([f"{[len(res)]}", f"{i+1}:", "Case"])
        else:res.extendleft([f"{i+1}:", "Case"])
        print(' '.join(res))#,file=f)
    #f.close()

imprimir()