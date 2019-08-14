# Funcs
def getNextPrime():
    num = listOfPrime[-1]
    length = len(listOfPrime)
    num += 1        # 4 oldu
    while(True):
        for i in range(length):
            if(num%listOfPrime[i]==0):
                num += 1
                break
        if(i+1==length):
            break
    listOfPrime.append(num)

listOfPrime = [2]
number = 600851475143
index = 0

while(number!=1):
    if(number%listOfPrime[index]==0):
        number = number / listOfPrime[index]
    else:
        getNextPrime()
        index += 1
    
print("largest prime is", listOfPrime[-1])