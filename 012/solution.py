import sys
sys.path.insert(0, "../")
from tools import lenPositiveDivisors

num = 1
i = 2
while True:
    if lenPositiveDivisors(num) > 500:
        break
    num += i
    i += 1

print(num)
