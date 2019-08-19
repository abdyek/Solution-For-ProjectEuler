sum = 0

for i in range(0, 334): # O(1)
    sum += i * 3

for i in range(0, 200): # 0(1)
    if(i%3):
        sum += i*5

print(sum)

