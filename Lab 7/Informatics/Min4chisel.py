def mini(a, b, c, d):
    return min(a, b, c, d)


nums = map(int, input().split())
arr = list(nums)
print(mini(arr[0], arr[1], arr[2], arr[3]))
