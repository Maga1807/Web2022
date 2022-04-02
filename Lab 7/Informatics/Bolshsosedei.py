n = int(input())
nums = map(int, input().split())
a = list(nums)
c = 0
for i in range(1,n-1):
    if a[i-1] < a[i] and a[i] > a[i+1]:
        c += 1
print(c)
