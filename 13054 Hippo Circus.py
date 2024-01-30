#Juan José Aguado
#30-01-2024

def execute(n,h,ta,td,hipos):
    hipos.sort()
    small = 0 #we start by trying to pair the smallest hippo with the bigger one
    big = n-1
    time = 0
    while small <= big:
        if hipos[small] + hipos[big] >= h or big == small:
            big -= 1
            time += ta
        else:
            time += td
            small += 1
            big -= 1
    time = min(time,ta*n)
    return time


def read():
    cases = int(input())
    for i in range(cases):
        n, h,ta,td = input().split()
        hipos = [int(x) for x in input().split()]
        print(f"Case {i+1}: {execute(int(n),int(h),int(ta),int(td),hipos)}")

read()