n = int(input())
nums = map(int, input().split())
a = list(nums)
for i in range(1, n):
    if (a[i-1] < 0 and a[i] < 0) or (a[i-1] > 0 and a[i] > 0):
        print('YES')
        break
    if i + 1 == n:
        print('NO')
