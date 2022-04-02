def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


def sum_double(a, b):
    if a != b:
        return a + b
    else:
        return 2 * (a + b)


def diff21(n):
    if n <= 21:
        return 21 - n
    elif n > 21:
        return 2 * (n - 21)


def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


def makes10(a, b):
    if (a == 10 or b == 10) or (a + b == 10):
        return True
    else:
        return False


def near_hundred(n):
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)


def pos_neg(a, b, negative):
    if (a < 0 and b > 0 and not negative) or (a > 0 and b < 0 and not negative) or (a < 0 and b < 0 and negative):
        return True
    else:
        return False


def not_string(str):
    s = str[0:3]
    if s == 'not':
        return str
    else:
        return 'not ' + str


def missing_char(str, n):
    if n < len(str):
        return str[:n] + str[n + 1:]


def front_back(str):
    if len(str) < 2:
        return str

    return str[-1] + str[1:-1] + str[0]


def front3(str):
    if len(str) < 3:
        return 3 * str
    return str[0:3] * 3
