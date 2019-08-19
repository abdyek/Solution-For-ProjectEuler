listOfPrime = [2]

def getNextPrime():
    number = listOfPrime[-1]
    number += 1
    dividing = listOfPrime[0]
    index = 0
    while(True):
        if(number%dividing==0):
            number += 1
            index = 0
            dividing = listOfPrime[index]
        elif(dividing>pow(number, 0.5)):
            break
        else:
            index +=1
            dividing = listOfPrime[index]
    listOfPrime.append(number)

def getNPrime(N):
    for i in range(N-1):
        getNextPrime()

getNPrime(10001)
print(listOfPrime[-1])