#Juan José Aguado
#Código 8957833
#Fecha 14-02-2023

# Task Description
"""
This is year 2200AD. Science has progressed a lot in two hundred years. Two hundred years is mentioned here because this
problem is being sent back to 2000AD with the help of time machine. Now it is possible to establish direct connection
between man and computer CPU. People can watch other peoples dream on 3D displayer (That is the monitor today) as if
they were watching a movie. One problem in this century is that people have become so dependent on computers that their
analytical ability is approaching zero. Computers can now read problems and solve them automatically. But they can solve
only difficult problems. There are no easy problems now. Our chief scientist is in great trouble as he has forgotten the
number of his combination lock. For security reasons computers today cannot solve combination lock related problems. In
a mid-summer night the scientist has a dream where he sees a lot of unsigned integer numbers flying around. He records
them with the help of his computer, Then he has a clue that if the numbers are (X1, X2, . . . , Xn) he will have to find an
integer number A (This A is the combination lock code) such that

(|X1 − A| + |X2 − A| + . . . + |Xn − A|)

is minimum.
Input
Input will contain several blocks. Each block will start with a number n (0 < n ≤ 1000000) indicating how many numbers
he saw in the dream. Next there will be n numbers. All the numbers will be less that 65536. The input will be terminated
by end of file.
The input must be read from standard input.
Output
For each set of input there will be one line of output. That line will contain the minimum possible value for A. Next it will
contain how many numbers are there in the input that satisfy the property of A (The summation of absolute deviation from
A is minimum). And finally you have to print how many possible different integer values are there for A (these values need
not be present in the input).
These numbers will be separated by single space.
The output must be written to standard output.
"""

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
