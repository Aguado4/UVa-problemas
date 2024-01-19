#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

def eje(lvl,mem):
    if lvl in mem: ans = mem[lvl]
    else:
        ans = eje(lvl-1,mem) + eje(lvl-2,mem)
        mem[lvl] = ans
    return ans

def imprimir():
    entrada = int(input())
    mem = {1:1,2:1}
    while entrada != 0:
        print(eje(entrada,mem))
        entrada = int(input())
imprimir()