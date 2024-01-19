#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

def eje(zap, n, lis):
    i, ans = 0,0
    while i < n-2:
        if lis[i] != lis[i+1]:
            ans +=1
            if zap[lis[i]][0] != i: ind1 = zap[lis[i]][0]
            else:ind1 = zap[lis[i]][1]
            ind2 = i+1
            lis[ind1] = lis[i+1]
            lis[i+1] = lis[i]
            zap[lis[i]][1] = ind2
            if zap[lis[ind1]][0] == i+1: zap[lis[ind1]][0] = ind1
            else: zap[lis[ind1]][1] = ind1
        i += 2
    return ans

def imprimir():
    #f = open("zap.txt","w")
    numcas = int(input())
    for i in range(numcas):
        entrada = input().split()
        dic, n, cant = dict(), len(entrada)-1, int(entrada.pop(0))
        for i in range(cant*2):
            if entrada[i] in dic:dic[entrada[i]].append(i)
            else: dic[entrada[i]] = [i]
        print(eje(dic,n,entrada))#, file = f)
    #f.close()
imprimir()