import math
x = int(input())
s = 0
a = int(math.log10(x))+1
for _ in range(a):
    s += x % 10
    x = x // 10
print(s)