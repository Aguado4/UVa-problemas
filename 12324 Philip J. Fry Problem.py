#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023
from sys import stdin 

def memo(t,e,le,lt,mem):
    if (t,e) in mem: ans = mem[(t,e)]
    else:
        if t == len(lt): ans = 0
        else:
            if e == 0: ans = lt[t] + memo(t+1,le[t],le,lt,mem)
            else: ans = min(lt[t] + memo(t+1,e+le[t],le,lt,mem) , lt[t]//2 + memo(t+1, e+ le[t] -1,le,lt,mem))
        mem[t,e] = ans
    return ans

def imprimir():
    entrada = int(input())
    while(entrada != 0):
        t , e, mem = [], [], dict()
        for i in range(entrada):
            tripes = input().split()
            t.append(int(tripes[0]))
            e.append(int(tripes[1]))
        print(memo(0,0,e,t,mem))
        entrada = int(input())
imprimir()