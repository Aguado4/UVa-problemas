from collections import deque
def check(A,K,val):
    K -= 1
    ans,n,k,curr = True,0,0,0
    while n != len(A) and ans:
        if A[n]>val:ans=False
        else:
            if (curr + A[n])<= val:
                curr,n = curr+A[n],n+1
            elif (curr + A[n]) > val and k < K:
                curr,k = A[n], k+1
                n += 1
            else:
                curr, n = curr + A[n], n + 1
            if curr > val: 
                ans = False
    return ans
def rec(A, k):
    low, hi = 0, sum(A)
    while low+1!=hi:
        mid = low+((hi-low)>>1)
        if check(A,k,mid): 
            hi = mid
        else: low = mid
    ans, suma, cont  = [], 0, 0
    A.reverse()
    while cont < len(A):
        suma += A[cont]
        if (suma > hi and k - 1 > 0) or (k - 1 >= len(A)-cont and k-1 > 0):
            ans.append("/")
            ans.append(A[cont])
            suma = A[cont]
            k -= 1
        else:
            ans.append(A[cont])
        cont += 1
    ans.reverse()
    return ans
def imprimir():
    casos = int(input())
    for i in range(casos): #hacemos el numero de casos que nos digan
        ent = [int(x) for x in input().split()]
        escribas = ent[1]
        libros = [int(x) for x in input().split()]
        salida = ""
        res = rec(libros, escribas)
        for j in range(len(res)):
            if j == len(res)-1: salida += "%s"%res[j]
            else:
                salida += "%s "%res[j]
        print(salida)
imprimir()