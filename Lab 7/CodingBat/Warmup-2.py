def string_times(str, n):
    return str * n


def front_times(str, n):
    if len(str) <= 3:
        return str * n
    return str[:3] * n


def string_bits(str):
    s = ''
    for i in range(len(str)):
        if i % 2 == 0:
            s += str[i]
    return s


def string_splosion(str):
    s = ''
    for i in range(len(str)):
        s += str[:i + 1]
    return s


def last2(str):
    if len(str) < 2:
        return 0
    s = str[len(str) - 2:]
    c = 0
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == s:
            c += 1
    return c


def array_count9(nums):
    c = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            c += 1
    return c


def array_front9(nums):
    a = False
    for i in range(len(nums)):
        if nums[i] == 9 and i < 4:
            a = True
    return a


def array123(nums):
    a = False
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            a = True
    return a


def string_match(a, b):
    m = min(len(a), len(b))
    c = 0
    for i in range(m - 1):
        if a[i:i + 2] == b[i:i + 2]:
            c += 1
    return c
