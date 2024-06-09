#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
Andy has n pairs of shoes in n different colors. At the end of the day, he likes to put them back on his shoe rack. He has
learned to always put a left shoe together with a right shoe. However, he has not learned about putting pairs of shoes with
the same color together. Papa’s job is to pair up the shoes. Since Papa is tired from work at the algorithm factory, he wants
to do this in the minimal number of steps. One step means to swap two shoes.
Your job is to help Papa.

Input
The first line contains the number of test cases. Each test case consists of a single line starting with the total number of pairs of
shoes n. The following 2n numbers describe the initial arrangement of shoes on the rack. Each shoe is labeled by a positive
integer at most 10 000 where two shoes share the same label if and only if they are part of the same pair. Both the left and
right shoes of a given pair will be present (remember that left and right shoes alternate).

Output
For each test case, output one line containing a single number – the minimum number of swaps needed to pair up all
shoes.
"""

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
