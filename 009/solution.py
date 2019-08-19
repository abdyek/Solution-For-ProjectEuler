def find():
    # a < b < c
    a = 1
    b = 2
    while True:
        # a + b + c = 1000 and a^2 + b^2 = c^2  - I simplified it -> a+b-500 = a * b / 1000
        if( a + b - 500 == a * b / 1000):
            break
        else:
            b += 1
            if(b==500):
                a += 1
                b = a
    c = int(pow(pow(a, 2) + pow(b, 2), 0.5))
    return  a * b * c

print(find())