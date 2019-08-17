# The sum of the squares of the first n number ->
#       1^2 + 2^2 + 3^2 + ... + n^2 = n * (n+1) * (2n+1) / 6
# The square of the sum of the first n number -->
#       1 + 2 + 3 + ... + n = n * (n+1) / 2
# I simplified these

def get(n):
    return (3 * pow(n,4) + 2 * pow(n,3) - 3 * pow(n,2) - 2 * n) / 12

print(get(100))
