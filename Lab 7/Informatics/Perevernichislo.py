import math
x = int(input())
a = int(math.log10(x))+1
c = 0
for i in range(a):
    b = x % 10
    x = x // 10
    c = c * 10 + b
print(c)
