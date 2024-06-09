#Juan José Aguado
#Código 8957833
#Fecha 20-04-2023

"""
You are helping the problem setters of International Creating Palindrome Contest(ICPC) in problem setting for the upcoming contest. 
In ICPC contestants are given some problems. Each problem is an integer sequence. The goal of the contestants is to convert the sequence into a palindromic integer sequence. 
A palindromic integer sequence is an integer sequence that is the same sequence when written from forwards or backwards, i.e., of the form {a1, a2, a3, . . . , a3, a2, a1}. 
Some examples of palindromic sequences are {78, 91, 78}, {100}, {10, 20, 20, 10}, {5, 5} etc. But {1, 2, 3, 1}, {10, 20} are not palindromic sequence. 
You can convert {1, 2, 3, 1} to a palindromic sequence by inserting a 2 at 4-th position which will become {1, 2, 3, 2, 1} and you can convert {10, 20} to palindromic sequence 
by inserting 20 at first or inserting 10 at last.
As contestant will be given problems(Integer sequences) with different difficulties, problem setters are asked to create problems of different difficulties. 
The difficulty of a problem is represented by an integer, for example, 0, 1, 2, 3, . . . , etc.
The difficulty of a problem is D, if at least D insertions of integer required to convert the given sequence into palindromic sequence.
Problem setters are also asked to give problems with difficulty not greater than K. 
Your job is to determine the difficulty of a given sequence to help the problem setters. 
If the given sequence is already a palindrome, it cannot be used in the contest. So you have to answer ‘Too easy’ without quotes. 
If the difficulty of the given sequence is more than K, that problem also cannot be used. 
In that case you have to answer ‘Too difficult’ without quotes. Otherwise you just have to answer the difficulty.

Input
Input will start with an integer T (T ≥ 1), number of test cases. Each test case starts with two integers N (1 ≤ N ≤ 10 000) and K (0 ≤ K ≤ 20), the length of integer sequence and maximum allowed difficulty

Output
For each test case, output a single line of the form ‘Case X: D’. Here X is the case number. If the given sequence is already a palindromic sequence D will be ‘Too easy’ without quotes, 
if the difficulty of the given sequence is greater than K, D will be ‘Too difficult’, other wise D will be the difficulty of the given sequence. See the sample input and output for exact format.
"""
opt = None

def eje(diff,cad,i,j,sol):
    global opt
    if i>=j:
        if (opt == None or sol < opt): opt = sol
    else:    
        if cad[i] == cad[j]: eje(diff,cad,i+1,j-1,sol)
        elif sol < diff and (opt == None or sol < opt):
                sol += 1
                eje(diff,cad,i+1,j,sol)
                eje(diff,cad,i,j-1,sol)
    

def imprimir():
    #f = open("pal.txt","w")
    global opt
    numcas = int(input())
    for i in range(numcas):
        length,diff = input().split()
        cad = [x for x in input().split()]
        opt = None
        eje(int(diff),cad,0,len(cad)-1,0)
        if opt == 0:
            print("Case %d: Too easy"%(i+1))#,file=f)
        elif opt == None:
            print("Case %d: Too difficult"%(i+1))#,file=f)
        else:
            print("Case %d: %d"%(i+1,opt))#,file=f)
    #f.close()
imprimir()
