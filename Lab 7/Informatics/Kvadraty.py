import math
a = int(input())
b = int(input())

for i in range(a, b+1):
    if i > 0 and i // math.sqrt(i) == math.sqrt(i):
        print(i)
