import sys
sys.path.insert(0, "../")
from tools import factorial

def get(n):
    #  n! / ((n/2 !) * (n/2 !))  = (n * (n-1) * (n-2) * (n-3) .... ((n/2)+1)) / ((n/2)!)
    #                              ------------------ t ---------------------
    t = 1
    for i in range(n, int(n/2), -1):
        t *= i
    return int(t / factorial(int(n/2)))

print(get(40))
