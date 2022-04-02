def double_char(str):
    a = ''
    for i in range(len(str)):
        a += str[i] * 2
    return a


def count_hi(str):
    c = 0
    for i in range(len(str) - 1):
        if str[i] + str[i + 1] == 'hi':
            c += 1
    return c


def cat_dog(str):
    c = 0
    d = 0
    for i in range(len(str) - 2):
        if str[i:i + 3] == 'cat':
            c += 1
        if str[i:i + 3] == 'dog':
            d += 1

    if c == d:
        return True
    else:
        return False


def count_code(str):
    c = 0
    for i in range(len(str) - 3):
        if str[i:i + 2] == 'co' and str[i + 3] == 'e':
            c += 1
    return c


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if b.endswith(a) or a.endswith(b):
        return True
    else:
        return False


def xyz_there(str):
    a = False
    for i in range(len(str) - 2):
        if str[i:i + 3] == 'xyz' and str[i - 1] != '.':
            a = True
    return a
