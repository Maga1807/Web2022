n = int(input())
nums = map(int, input().split())
a = list(nums)
for i in range(n):
    print(a[n - i - 1], end=' ')

