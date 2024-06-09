#Juan José Aguado
#Código 8957833
#Fecha 17-04-2023

"""
Here is an odd little puzzle which occurred the other day at an archery meeting. The young lady who carried off the first prize scored exactly one hundred points.
Can you figure out how many arrows she used, as well as the points awarded to each arrow?
You will receive a list of N positive integers P1, P2, ..., PN, which represent the scores in the archery target; that is, the different scores that can be achieved with a single hit.
You will also receive an integer S, which is the total score that is to be obtained.
Determine the minimum number of arrows necessary to score S points, and print the points awarded to each of those arrows, sorted in descending order. 
If there is more than one group of arrows that provide a valid solution, choose the solution for which the first arrow scores the highest amount of points; if the solution is still not unique, 
then choose one in which the second arrow scores the highest score possible, and keep applying this reasoning for the rest of the arrows.

Input:
Input starts with a positive integer T, that denotes the number of test cases. Each test case starts with two integers in a single line: N and S. 
The second line for each test case contains N integers in ascending order: P1, P2, ..., PN. You can assume: 1 ≤ N ≤ 50 and 1 ≤ P1 < P2 < P3 < ... < PN ≤ S ≤ 300.
The input must be read from standard input.

Output:
For each test case, print the case number, followed by the minimum number of arrows required to score S points between square brackets and then the sequence of points for each arrow, in descending order. 
These scores must be separated by single spaces. If the test case does not have a solution, simply print the case number, followed by the string 'impossible'.
"""

from collections import deque
opt = None
def eje(tot, points,n,sol):
    global opt
    if not (opt != None and opt != ["impossible"] and len(opt) == 1): #acaba en caso de que solo una flecha basta
        if tot == 0:
            if opt == None or len(sol) < len(opt):
                opt = list(sol)
        else:
            if not (opt != None and opt != ["impossible"] and len(sol)>=len(opt)):
                while n > -1:
                    if tot >= points[n] and (tot - points[n] >= points[0] or tot - points[n] == 0):
                        sol.append(points[n])
                        eje(tot-points[n],points,n,sol)
                        sol.pop()
                    n -= 1
                if sol == [] and opt == None: opt = ["impossible"]
    return opt

def imprimir():
    #f = open("arch.txt","w")
    global opt
    numcas = int(input())
    for i in range(numcas):
        N,S = input().split()
        points = [int(x) for x in input().split()] 
        sol = []
        opt = None
        res = deque(map(str,eje(int(S),points,len(points)-1,sol)))
        if res[0] != "impossible": res.extendleft([f"{[len(res)]}", f"{i+1}:", "Case"])
        else:res.extendleft([f"{i+1}:", "Case"])
        print(' '.join(res))#,file=f)
    #f.close()

imprimir()
