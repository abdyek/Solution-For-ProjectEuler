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

def lenPositiveDivisors(number):
    length = 1
    primeFactor = getPrimeFactor(number)
    for prime in primeFactor:
        length *= (primeFactor[prime] + 1)
    return length

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result
