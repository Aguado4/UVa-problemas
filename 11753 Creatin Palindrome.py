#Juan José Aguado
#Código 8957833
#Fecha 20-04-2023

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