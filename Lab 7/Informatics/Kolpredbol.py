n = int(input())
nums = map(int, input().split())
a = list(nums)
c = 0
for i in range(1,n):
    if a[i-1] < a[i]:
        c += 1
print(c)
