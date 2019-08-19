listOfPrime = [2]
summation = 2

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
    if number > 2000000:
        return False
    else:
        listOfPrime.append(number)
        global summation
        summation += number
        return True
    
while(getNextPrime()):
    pass

print(summation)