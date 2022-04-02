def make_bricks(small, big, goal):
    if small + 5 * big < goal or goal % 5 > small:
        return False
    else:
        return True


def lone_sum(a, b, c):
    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c


def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if (n >= 13 and n < 15) or (n > 16 and n <= 19):
        return 0
    else:
        return n


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if num % 10 >= 5:
        return num + 10 - num % 10
    elif num % 10 < 5:
        return num - num % 10


def close_far(a, b, c):
    if abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(b - c) >= 2 and abs(a - b) >= 2:
        return True
    else:
        return False


def make_chocolate(small, big, goal):
    if small + 5 * big < goal or goal % 5 > small:
        return -1
    elif goal / 5 >= big:
        return goal - big * 5
    else:
        return goal % 5
