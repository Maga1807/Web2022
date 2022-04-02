def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) - 1] == 6:
        return True
    else:
        return False


def same_first_last(nums):
    a = False
    for i in range(len(nums)):
        if nums[0] == nums[len(nums) - 1]:
            a = True
        else:
            a = False
    return a


def make_pi():
    return [3, 1, 4]


def common_end(a, b):
    if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
        return True
    else:
        return False


def sum3(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
    return s


def rotate_left3(nums):
    s = nums[0]
    nums[0] = nums[1]
    nums[1] = nums[2]
    nums[2] = s
    return nums


def reverse3(nums):
    s = nums[0]
    nums[0] = nums[2]
    nums[2] = s
    return nums


def max_end3(nums):
    a = max(nums[0], nums[2])
    for i in range(len(nums)):
        nums[i] = a
    return nums


def sum2(nums):
    a = 0
    if len(nums) > 1:
        a = nums[0] + nums[1]
    elif len(nums) == 1:
        a = nums[0]
    return a


def middle_way(a, b):
    return [a[1], b[1]]


def make_ends(nums):
    return [nums[0], nums[-1]]


def has23(nums):
    if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3:
        return True
    else:
        return False
