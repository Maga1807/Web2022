# 1
print("Hello, World!")

# 2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# 4
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)


# 5
def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))

# 6
if __name__ == '__main__':
    n = int(input())
    i = 1
    while i <= n:
        print(i, end='')
        i += 1

# 7
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    s = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(s)

# 8
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    a = list(set(arr))
    a.sort()
    print(a[-2])


# 9
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello %s %s! You just delved into python.' % (first_name, last_name))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# 10
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
