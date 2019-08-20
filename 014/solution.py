# not optimize
num = 1
index = num
longestChain = 0
longestIndex = 0

while index < 1000000:
    chain = [num]
    while num!=1:
        if(num%2==0):
            num = num / 2
        else:
            num = num * 3 + 1
        chain.append(num)
    if(len(chain) > longestChain):
        longestChain = len(chain)
        longestIndex = index
    index += 1
    num = index

print(longestIndex, " - ", longestChain)