# Task Description
"""
Before the invention of book-printing, it was very hard to make a copy of a book. All the contents had to be re-written by
hand by so called scribers. The scriber had been given a book and after several months he finished its copy. One of the
most famous scribers lived in the 15th century and his name was Xaverius Endricus Remius Ontius Xendrianus (Xerox).
Anyway, the work was very annoying and boring. And the only way to speed it up was to hire more scribers.
Once upon a time, there was a theater ensemble that wanted to play famous Antique Tragedies. The scripts of these
plays were divided into many books and actors needed more copies of them, of course. So they hired many scribers to
make copies of these books. Imagine you have m books (numbered 1, 2, . . . , m) that may have different number of pages
(p1, p2, . . . , pm) and you want to make one copy of each of them. Your task is to divide these books among k scribes, k ≤
m. Each book can be assigned to a single scriber only, and every scriber must get a continuous sequence of books. That
means, there exists an increasing succession of numbers 0 = b0 < b1 < b2, . . . < bk−1 ≤ bk = m such that i-th scriber gets a
sequence of books with numbers between bi−1 + 1 and bi

. The time needed to make a copy of all the books is determined by
the scriber who was assigned the most work. Therefore, our goal is to minimize the maximum number of pages assigned to
a single scriber. Your task is to find the optimal assignment.

Input
The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case
consists of exactly two lines. At the first line, there are two integers m and k, 1 ≤ k ≤ m ≤ 500. At the second line, there are
integers p1, p2, . . . , pm separated by spaces. All these values are positive and less than 10000000.
The input must be read from standard input.

Output
For each case, print exactly one line. The line must contain the input succession p1, p2, . . . , pm divided into exactly k parts
such that the maximum sum of a single part should be as small as possible. Use the slash character (’/’) to separate the
parts. There must be exactly one space character between any two successive numbers and between the number and the
slash.
If there is more than one solution, print the one that minimizes the work assigned to the first scriber, then to the second
scriber etc. But each scriber must be assigned at least one book.
"""

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
