def double_power(c, d):
    f = pow(c, d)
    return f


nums = map(float, input().split())
a = list(nums)
print(double_power(a[0], a[1]))
