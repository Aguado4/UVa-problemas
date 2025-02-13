#Juan José Aguado
#Código 8957833
#Fecha 17-04-2023
#This is the link for the problem description: http://poj.org/problem?id=1011

"""
George took sticks of the same length and cut them randomly until all parts became at most 50 units long. 
Now he wants to return sticks to the original state, but he forgot how many sticks he had originally and how long they were originally. 
Please help him and design a program which computes the smallest possible original length of those sticks. 
All lengths expressed in units are integers greater than zero.

Input
The input file contains blocks of 2 lines. 
The first line contains the number of sticks parts after cutting. 
The second line contains the lengths of those parts separated by the space. 
The last line of the file contains ‘0’.

Output
The output file contains the smallest possible length of original sticks, one per line.
"""

cond = False
def check(part,actsum,i,usa,ind,indos,numpal,tot):
    global cond
    if not cond:
        if actsum == i:
            numpal += 1
            if numpal == tot/i : cond = True
            else: check(part,0,i,usa,ind+1,ind + 1,numpal,tot)
        elif ind != len(part):
            if not usa[ind]: #si es el primer caso
                actsum = part[ind]
                usa[ind] = True
            if part[ind] == i:
                check(part,part[ind],i,usa,ind,indos,numpal,tot)
            else:
                j = indos
                while j < len(part) and not cond:
                    if not usa[j] and actsum + part[j] <= i and (i-(actsum+part[j]) == 0 
                    or i-(actsum+part[j]) >= part[len(part)-1]):
                        usa[j] = True
                        check(part, actsum + part[j],i,usa,ind,j,numpal,tot)
                        usa[j] = False
                    j += 1

def eje(part,tot,usa):
    global cond
    opt = float('inf')
    i = part[0]
    while i <= tot and cond == False:
        if tot%i == 0 and (part[0] == i or part[0]+part[len(part)-1] <= i):
            temp = list(usa)
            check(part,0,i,temp,0,0,0,tot)
        i += 1
    return i-1

def imprimir():
    #f = open("pal.txt","w")
    global cond
    numpar = int(input())
    while numpar != 0:
        part = [int(x) for x in input().split()] 
        usa = [False for x in range(len(part))]
        tot = sum(part)
        part.sort(reverse = True)
        cond = False
        print(eje(part,tot,usa))#,file=f)
        numpar = int(input())
    #f.close()

imprimir()
