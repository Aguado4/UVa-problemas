#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

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