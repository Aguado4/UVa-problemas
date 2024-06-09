#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
Carlos is very concerned with the environment. Whenever possible, he tries to use less polluting means of transport. He
recently got a job close to home and is now using his bike to go to work.
Unfortunately, in the route between his home and his job there is a nail factory, and often some nails fall from their
trucks, and end up puncturing Carlos’ bike tires. Therefore he ends up having to make several patches on the tires of his
bike.
To make the repairs, Carlos uses two different types of patches. Both types are as wide as a bike tire, but differ in length.
As the cost of the patch is proportional to its length, Carlos is trying to find a way to save money, using the least possible
length of patches to make the repairs, without cutting the patches.
The first step in repairing a tire is making a chalk mark on a position of the tire and then writing down the distances,
measured clockwise, of each of the holes in relation to the chalk mark. Each hole must be completely covered by a
patch. Carlos would like your help to determine, given the positions of the holes, the most economic way to make the
repair.

Input
The input contains several test cases. Each test case is composed of two lines. The first line contains four integers N,
C, T1, and T2. Integer N indicates the number of holes in the tire and C indicates the cirunference length of the tire, in
centimeters. The lengths of the patches in centimeters are given by integers T1 and T2. The second line contains N integers
Fi, representing the distance, in clockwise direction, from the chalk mark to hole i, in centimeters.

Output
For each test case your program must print a single line, containing a single integer, the smallest total length of patches
needed to make all the repairs.
"""

from sys import stdin
from collections import deque

def eje(n,p1,p2,hue,mem):
    if n in mem: ans = mem[n]
    else:
        if n == len(hue): ans = 0
        else:
            pn1,pn2 = n,n
            while pn1 < len(hue)-1 and hue[pn1+1] <= hue[n]+p1:
                pn1 += 1 
            while pn2 < len(hue)-1 and hue[pn2+1] <= hue[n]+p2:
                pn2 += 1 
            ansp1 = eje(pn1+1,p1,p2,hue,mem) + p1
            ansp2 = eje(pn2+1,p1,p2,hue,mem) + p2
            ans = min(ansp1,ansp2)
        mem[n] = ans
    return ans

def cic(c,p1,p2,hue):
    min = float('inf')
    hue = [x-hue[0] for x in hue]
    if len(hue) > 1:
        for i in range(len(hue)):
            mem = dict()
            res = eje(0,p1,p2,hue,mem)
            if res < min: min = res
            hue = deque(x-hue[1] for x in hue)
            hue.append(hue.popleft()+c) 
    else:
        mem = dict()
        min = eje(0,p1,p2,hue,mem)
    return int(min)


def imprimir():
    #f = open("patches.txt","w")
    entrada = stdin.readline()
    while entrada != "":
        entrada = entrada.split()
        n,c = entrada[0],int(entrada[1]) #numero de huecos,circunferencia de la llanta
        p1,p2 = int(entrada[2]), int(entrada[3]) #parches
        hue = [int(x) for x in input().split()] #coordenadas de los huecos
        print(cic(c,p1,p2,hue))#,file=f)
        entrada = stdin.readline()
    #f.close()
imprimir()
