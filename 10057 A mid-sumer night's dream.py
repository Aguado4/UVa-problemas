#Juan José Aguado
#Código 8957833
#Fecha 14-02-2023
from sys import stdin
def busquedaBin(A,low,hi,v):
    ans = -1
    if low == hi:ans = -1
    elif low + 1 == hi: 
        if A[hi] == v:ans = hi
    else:
        mid = (low + hi)// 2
        if A[mid] >= v:ans = busquedaBin(A, low, mid, v)
        else:ans = busquedaBin(A, mid, hi, v)
    return ans

def absum(nums, val):
    suma = 0
    for i in nums:
        suma += abs(i-val)
    return suma

def eje(nums):
    n = len(nums)
    ind = n // 2 if n % 2 == 1 else (n//2)-1
    med = may = nums[ind] 
    ind = busquedaBin(nums,-1,n-1,med)
    res = absum(nums,med) #restar med al ultimo valor que cumpla
    cond, cont= ind, 0
    while cond < n:
        comp = absum(nums,nums[cond]) 
        if nums[cond] == med or comp == res:
            cont +=1
            if nums[cond] > may: may = nums[cond]
        else: cond += n
        cond +=1
    tot = may-med + 1
    return(med, cont, tot)

def imprimir():
    #f = open("dr.txt","w")
    entrada = stdin.readline() #se recibe el numero de numeros que vio
    while (entrada != ""):#se ejecuta hasta el final de la entrada
        n = int(entrada)
        nums = []
        for i in range(n):
            nums.append(int(input()))
        nums.sort()
        res = eje(nums)
        print("%s %s %s" %(res[0], res[1], res[2]))#, file=f)
        entrada = stdin.readline()
    print("")#,file=f)
    #f.close()
imprimir()