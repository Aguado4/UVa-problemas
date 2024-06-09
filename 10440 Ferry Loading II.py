#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
Before bridges were common, ferries were used to transport cars across rivers. River ferries, unlike their larger cousins, run
on a guide line and are powered by the river’s current. Cars drive onto the ferry from one end, the ferry crosses the river,
and the cars exit from the other end of the ferry.
There is a ferry across the river that can take n cars across the river in t minutes and return in t minutes. A total of m cars
arrive at the ferry terminal by a given schedule. What is the earliest time that all the cars can be transported across the
river? What is the minimum number of trips that the operator must make to deliver all cars by that time?

Input
The first line of input contains c, the number of test cases. Each test case begins with n, t, m. Then m lines follow, each
giving the arrival time for a car (in minutes since the beginning of the day). The operator can run the ferry whenever he or
she wishes, but can take only the cars that have arrived up to that time.

Output
For each test case, output a single line with two integers: the time, in minutes since the beginning of the day, when the last
car is delivered to the other side of the river, and the minimum number of trips made by the ferry to carry the cars within
that time. You may assume that 0 < n, t, m < 1440. The arrival times for each test case are in non-decreasing order.
"""

from math import ceil

def eje(n,t,c):
    cant, act, cont = len(c), 0, n - 1
    if cant % n == 0:
        while cont < cant:
            if cont != cant - 1: act = max(act,c[cont]) + 2 * t
            else: act = max(act,c[cont]) + t 
            cont += n
        ans = (act,max(cant/n,1))
    else:
        cont = (cant % n) - 1
        act = c[cont] + 2 * t
        cont += n
        while cont < cant:
            if cont != cant - 1: act = max(act,c[cont]) + 2 * t
            else: act = max(act,c[cont]) + t
            cont += n
        ans = (act, ceil(cant/n))
    return ans

def imprimir():
    #f = open("fer.txt","w")
    numcas = int(input())
    for i in range(numcas):
        n,t,m = input().split()
        c = []
        for j in range(int(m)):
            c.append(int(input()))
        c.sort()
        if int(n) >= int(m): res = (c[-1] + int(t),1)
        else:res = eje(int(n),int(t),c)
        print("%d %d"%(res[0],res[1]))#,file = f)
    #f.close()
imprimir()
