sumOfEven = 0
small = 1
big = 2
while(big<4000000):
    if(big%2==0):
        sumOfEven += big
    big, small = small + big, big

print(sumOfEven)

