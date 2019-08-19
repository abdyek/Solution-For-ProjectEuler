
def controlPalindrome(number):  # Only 6 digit
    numList = list(str(number))
    palindrome = False
    if(numList[0]==numList[-1]):
        if(numList[1]==numList[-2]):
            if(numList[2]==numList[-3]):
                palindrome = True
    return palindrome

    

multiplier2 = 999
multiplier1 = 999


while(not (multiplier1==800 and multiplier2==800)):
    number = multiplier1 * multiplier2
    if(controlPalindrome(number)):
        break
    else:
        multiplier2 -= 1
        if(multiplier2==800):
            multiplier1 -= 1
            multiplier2 = multiplier1

number = multiplier1 * multiplier2
print(number)

