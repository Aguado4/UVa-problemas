#Juan José Aguado
#Código 8957833
#Fecha 17-04-2023
orde = []
opt = float('inf')
cont = 0

def eje(map,swaps,ord):
    global opt
    global orde
    global cont
    if map == orde: opt, cont = swaps, cont+1
    elif swaps < opt:
        for i in range(len(map)-1):
            if map[i]>map[i+1]:
                map[i],map[i+1] = map[i+1],map[i]
                ord.append(i)
                eje(map,swaps+1,ord)
                ord.pop()
                map[i],map[i+1] = map[i+1],map[i]

def imprimir():
    #f = open("swp.txt","w")
    global orde
    global opt
    global cont
    map,cnt =[int(x) for x in input().split()], 1
    while len(map) != 1 and map[0] != 0:
        map = map[1:]
        orde = sorted(map)
        if map == orde: print("There are 0 swap maps for input data set %d."%cnt)#,file=f)
        else: 
            eje(map,0,[])
            print("There are %d swap maps for input data set %d."%(cont,cnt))#,file=f)
        cont,opt,map,cnt = 0, float('inf'), [int(x) for x in input().split()], cnt + 1
    #f.close()
imprimir()