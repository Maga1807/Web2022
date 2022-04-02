def xor(x, y):
    return x ^ y


nums = map(int, input().split())
a = list(nums)
print(xor(a[0], a[1]))
