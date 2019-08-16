def isPrime(number):
    prime = True
    botLimit = 2
    topLimit = int(pow(number, 0.5)) + 1
    for i in range(botLimit, topLimit):
        if(number%i==0):
            prime = False
            break
    return prime
        
def getPrimeFactor(number):
    primeFactor = {}
    dividing = 2
    while(number!=1):
        if(number % dividing==0 and isPrime(dividing)):
            number = number / dividing
            if(dividing in primeFactor):
                primeFactor[dividing] += 1
            else:
                primeFactor[dividing] = 1
            
        else:
            dividing += 1
    return primeFactor

def getList(firstNumber, lastNumber):
    if(firstNumber<2):
        firstNumber = 2
    listOfNumber = {}
    for i in range(firstNumber, lastNumber+1):
        listOfNumber[i] = getPrimeFactor(i)
    return listOfNumber

def findMinNumber(listOfNumber):
    number = 1
    maxOfUpper = {}
    for i in listOfNumber:
        for prime in listOfNumber[i]:
            if prime in maxOfUpper:
                maxOfUpper[prime] = max(maxOfUpper[prime], listOfNumber[i][prime])
            else:
                maxOfUpper[prime] = listOfNumber[i][prime]
    for prime in maxOfUpper:
        number *= pow(prime, maxOfUpper[prime])
    return number



print(findMinNumber(getList(1,20)))