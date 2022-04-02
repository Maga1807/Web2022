def count_evens(nums):
    c = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            c += 1
    return c


def big_diff(nums):
    return max(nums) - min(nums)


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


def sum13(nums):
    c = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        c += nums[i]
        i += 1
    return c


def sum67(nums):
    a = True
    c = 0
    for i in range(len(nums)):
        if nums[i] == 6:
            a = False

        if a:
            c += nums[i]

        if nums[i] == 7:
            a = True

    return c


def has22(nums):
    a = False
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            a = True
    return a
