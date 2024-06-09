#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
It’s been a few months since Bender solved his famous bending problem. A special request has arrived to Planet Express
Inc., the interplanetary courier company where Bender works. Professor Farnsworth (founder, CEO, and chairman of the
board) immediately prepared the mission and summoned his crew: Philip J. Fry, Turanga Leela, and Bender. To succeed in
the mission, the crew has to make n trips τ1, τ2, . . . , τn, in the exact order established by Professor Farnsworth. He has also
provided the crew with a notebook that specifies how many minutes each trip in the spaceship will take.

Nibbler, Leela’s stupid pet, is also a member of the crew and a critical element to succeed in the mission. Nibbler’s feces,
which it expels every now and then, consist of spheres of dark matter that can be used to increase the speed of the spaceship.
In fact, a sphere used during a trip halves its duration. Bender’s role in the mission is to pick up the heavy spheres and put
them in the reactor of the spaceship. However, he will never put two spheres during the same trip: the accumulation of dark
matter is extremely dangerous and may destroy the spaceship.
In each trip of the mission, Nibbler expels a certain number of dark matter spheres that can be used to decrease the duration
of any of the upcoming trips. In other words, a sphere of dark matter produced during the trip τi can be used to duplicate
the speed of the spaceship in one of the trips τj, with i < j ≤ n.

Fry is responsible for planning how to use the spheres to reduce the total travel time. Your task is to help Fry in determining
what is the minimum duration of the mission if he uses Nibbler’s spheres cleverly.

Input
The input consists of several test cases. The first line of each case contains an integer n indicating the number of trips
(1 ≤ n ≤ 100). Then, n lines follow describing each of the trips τ1, τ2, . . . , τn: each line contains two integers ti and bi
separated by blanks, where ti (2 ≤ ti ≤ 1 000) indicates the duration in minutes specified by Professor Farnsworth for the
trip τi (ti is always even) and bi (0 ≤ bi ≤ n) indicates the number of dark matter spheres that Nibbler will expel during the
trip τi. The last test case is followed by a line containing a single ‘0’.

Output
For each test case, print a line with an integer number indicating the minimum time required to complete the mission.
"""

from sys import stdin 

def memo(t,e,le,lt,mem):
    if (t,e) in mem: ans = mem[(t,e)]
    else:
        if t == len(lt): ans = 0
        else:
            if e == 0: ans = lt[t] + memo(t+1,le[t],le,lt,mem)
            else: ans = min(lt[t] + memo(t+1,e+le[t],le,lt,mem) , lt[t]//2 + memo(t+1, e+ le[t] -1,le,lt,mem))
        mem[t,e] = ans
    return ans

def imprimir():
    entrada = int(input())
    while(entrada != 0):
        t , e, mem = [], [], dict()
        for i in range(entrada):
            tripes = input().split()
            t.append(int(tripes[0]))
            e.append(int(tripes[1]))
        print(memo(0,0,e,t,mem))
        entrada = int(input())
imprimir()
