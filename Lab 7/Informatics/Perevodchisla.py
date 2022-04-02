import math
n = int(input())
a = int(math.log10(n))+1
c = 0
for i in range(a):
    c += n % 10 * (2**i)
    n = n // 10
print(c)
