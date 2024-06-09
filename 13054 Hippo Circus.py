#Juan José Aguado
#30-01-2024

"""
You all know about my friend Hippo. Hippo and its other hippopotamus friends are starting a circus.
They have been practicing a lot, and they are getting better at the show. I have seen their show several
times and I personally think they are really good. So I encouraged them to show in public. And after
a lot of arguing and convincing they finally agreed.
So are they are getting ready for their big showdown. Everything is prepared. The performers are
working day and night to perfect everything. The tent is almost ready. In a word everything is having the final touch.
In the night before the show the hippopotamuses started to budget the time and encountered a big problem. They were planning for a big entrance where every
hippopotamus will enter through the gate and take a bow to the audience. But this is taking too much time.
So to shorten this they devised a plan — “One hippo will ride another one”. The balances of the hippopotamuses are not so good yet. So a hippo can take only
another hippo over it, not more than that. There is another problem, if a hippo carries another hippo, it slows the speed of the hippo. So to help them with the
problem they wish your help. Given a door with height H, and N hippopotamuses with height hi (height of the i-th hippo, 1 ≤ i ≤ N),
you need to find the minimum time so that every hippo can enter the door and bow. A hippo can only enter the door if its height is less than the height of the
door. If a hippo is carrying another hippo, then the summation of their heights must be less than the door’s height. A hippo while walking alone, takes Ta time to enter the door and bow. 
A hippo while carrying another hippo, takes Td time to enter and bow.

Input
First line of input will contain an integer, C (1 ≤ C ≤ 10), the number of test cases. Then C cases will
follow. First line of each case is four integers, N, H, Ta, and Td. Next line contains N integers, the
height of the hippopotamuses.
Here, 1 ≤ N ≤ 100000 and 0 ≤ Ta < Td ≤ 10000.
All the heights will be less than 100. Heights of all the hippopotamuses will be less than the H.

Output
For each case output one line. ‘Case X: M’ (without the quotes), where X is the case number starting
from 1 and M is minimum time needed.
"""
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
