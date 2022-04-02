import math
x = int(input())
d = int(input())
c = 0
a = int(math.log10(x))+1
for i in range(a):
    if x % 10 == d:
        c += 1
    x = x // 10
print(c)
