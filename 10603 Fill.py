#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
There are three jugs with volumes a, b, and c liters. (a, b, and c are positive integers not greater than 200). The first and
the second jugs are initially empty, while the third is completely filled with water. It is allowed to pour water from one jug
into another until either the first one is empty or the second one is full. This operation can be performed zero, one, or more
times.
You are to write a program that computes the least total amount of water that needs to be poured so that at least one of the
jugs contains exactly d liters of water (d is a positive integer not greater than 200). If it is not possible to measure d liters
this way, your program should find a smaller amount of water d0 < d, which is closest to d and for which d0 liters could be
produced. When d0 is found, your program should compute the least total amount of poured water needed to produce d0
liters in at least one of the jugs.

Input
The first line of input contains the number of test cases. In the next T lines, T test cases follow. Each test case is given in
one line of input containing four space-separated integers — a, b, c, and d.

Output
The output consists of two integers separated by a single space. The first integer equals the least total amount (the sum of
all waters you pour from one jug to another) of poured water. The second integer equals d if d liters of water could be
produced by such transformations, or equals the closest smaller value d0 that your program has found.
"""

import heapq

def mind(cas,d,dprim):
    d1,d2,d3 = float('-inf'), float('-inf'), float('-inf')
    if d > cas[0] and d - cas[0] <= d - dprim[0]: d1 = cas[0]
    if d > cas[1] and d - cas[1] <= d - dprim[0]: d2 = cas[1]
    if d > cas[2] and d - cas[2] <= d - dprim[0]: d3 = cas[2]
    if d1 == float('-inf') and d2 == float('-inf') and d3 == float('-inf'): ans = -1
    else: ans = max(d1,d2,d3)
    return ans
 
def eje(a,b,c,d):
    visitados, grafo, dprim = {(0,0,c):0}, [(0,(0,0,c))], [0,0]
    #todas las posibilidades
    ea,eb,ec = 0,0,c
    if d > c: ans = "0 %d"%c
    elif c > d and a >= c and b >= c: ans = "0 0"
    else:
        while len(grafo) > 0 and ea != d and eb != d and ec != d:
            ea,eb,ec = heapq.heappop(grafo)[1]
            #a->b
            cas = (max(0,ea-(b-eb)),min(b,ea+eb),ec)
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(b,ea+eb)-eb
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1: 
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
            #b->a
            cas = (min(a,ea+eb),max(0,eb-(a-ea)),ec)
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(a,ea+eb)-ea
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1:
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
            #a->c
            cas = (max(0,ea-(c-ec)),eb,min(c,ea+ec))
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(c,ea+ec) - ec
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1:
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
            #c->a
            cas = (min(a,ea+ec),eb,max(0,ec-(a-ea)))
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(a,ea+ec) - ea
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1: 
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
            #b->c
            cas = (ea,max(0,eb-(c-ec)),min(c,eb+ec))
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(c,ec+eb) - ec
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1:
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
            #c->b
            cas = (ea,min(b,eb+ec),max(0,ec-(b-eb)))
            if not cas in visitados:
                visitados[cas] = visitados[(ea,eb,ec)] + min(b,ec+eb) - eb
                heapq.heappush(grafo,(visitados[cas],cas))
                temp = mind(cas,d,dprim)
                if temp != -1:
                    if dprim[0] != temp or (dprim[0] == temp and visitados[cas] < dprim[1]): dprim = [temp,visitados[cas]]
        if ea != d and eb != d and ec != d: ans = "%d %d"%(dprim[1],dprim[0]) #en caso de que no se encontró d
        else: ans = "%d %d"%(visitados[(ea,eb,ec)], d) #en caso de que si
    return ans

def imprimir():
    #f = open("fill.txt","w")
    numcas = int(input())
    for i in range(numcas):
        a,b,c,d = input().split()
        print(eje(int(a),int(b),int(c),int(d)))#, file = f)
    #f.close()

imprimir()
