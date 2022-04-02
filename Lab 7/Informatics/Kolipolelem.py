n = int(input())
nums = map(int, input().split())
a = list(nums)
c = 0
for i in range(n):
    if a[i] > 0:
        c += 1
print(c)
