#Juan José Aguado
#Código 8957833
#Fecha 2-03-2023

# Task Description
"""
Robocops Inc. is a toy manufacturer company that develops a robot game in which a cop tries to catch a thief in a field that
is simulated with a rectangular grid whose coordinates are denoted by pairs of integers. The resulting pursuit occurs in a
discrete time scale: time is modeled with non-negative integers 0, 1, 2, . . ..
An object on the grid has a speed that determines how the object moves during the simulation. A speed is modeled with a
pair of integers. The first one is the horizontal speed and the second one is the vertical speed. Additionally, horizontal and
vertical speeds may vary in one unit (each one) to simulate slowing or accelerating.
More exactly: if at time k the object is at location (x, y) with speed (u, v), then, at time k + 1, the object may appear at
location (x`, y`) = (x + u + e, y + v + δ), for some e, δ ∈ {−1, 0, 1}. The speed at time k + 1 is (x` − x, y` − y). For an object that moves with constant speed the values  and δ are always 0.

At time 0, the cop is located at the origin of the grid, and the thief is at coordinates (a, 0). The thief is moving with a
constant speed; on the other hand, the cop starts still, but may vary his speed according to the given rules. Clearly, the cop
catches the thief at time k if at this time the positions of both coincide.
Your task is to develop a program to control the cop in order to catch the thief in an efficient way. Your algorithm should
determine the minimum time in which the cop may catch the thief.

Input
The problem input consists of several cases, each one defined by a line with three integer values, separated by blanks, that
stand for the initial position a of the thief in the X-axis (0 ≤ a ≤ 1 000), the horizontal speed u (0 ≤ u ≤ 10) and the vertical
speed v (0 ≤ v ≤ 10) at which he moves.

Output
Output texts for each input case preserve the order in the input file. For an input case, the output should be an integer that is
the minimum time at which the cop may catch the thief.
"""

from sys import stdin

def eje(a,u,v):
    pospol = [0,1] #x,y como si hubiera pasado una unidad de tiempo
    poslad = [a,v] #x,y se inicializa asi para que pueda entrar al ciclo
    x,y = 0,1 #velocidad del policia en x,y para que y pueda avanzar ya que empiezan iguales
    t,timx,timy = 0,0,1 #tiempo total,tiempo x, tiempo y en uno porque ya avanzo
    if a != 0:#evita que entre si empiezan en la misma posicion
        while pospol[0] < poslad[0] or pospol[1] < poslad[1]:
            #parte x
            if pospol[0] < poslad[0]:
                timx += 1
                poslad[0] += u
                x += 1
                pospol[0] += x 
            #parte y
            if pospol[1] < poslad[1]:
                timy += 1
                poslad[1] += v
                y += 1
                pospol[1] += y
        t = max(timx,timy) 
    return t

#10 4 7

def imprimir():
    entrada = stdin.readline()
    #f = open("catch.txt","w")
    while entrada != "":
        a,u,v = entrada.split()
        print(eje(int(a),int(u),int(v)))#, file = f)
        entrada = stdin.readline()
    #f.close()

imprimir()
