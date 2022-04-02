def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend and cigars >= 40 and cigars <= 60:
        return True
    else:
        return False


def date_fashion(you, date):
    if you >= 8 and date > 2:
        return 2
    elif date >= 8 and you > 2:
        return 2
    elif you < 8 and you > 2 and date > 2 and date < 8:
        return 1
    else:
        return 0


def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 90 and not is_summer:
        return True
    elif temp >= 60 and temp <= 100 and is_summer:
        return True
    else:
        return False


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed > 65 and speed <= 85:
            return 1
        else:
            return 2

    if not is_birthday:
        if speed <= 60:
            return 0
        elif speed > 60 and speed <= 80:
            return 1
        else:
            return 2


def sorta_sum(a, b):
    if a + b >= 10 and a + b < 20:
        return 20
    else:
        return a + b


def alarm_clock(day, vacation):
    if not vacation:
        if day >= 1 and day <= 5:
            return '7:00'
        else:
            return '10:00'

    if vacation:
        if day >= 1 and day <= 5:
            return '10:00'
        else:
            return 'off'


def love6(a, b):
    if a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6:
        return True
    else:
        return False


def in1to10(n, outside_mode):
    if not outside_mode:
        if n >= 1 and n <= 10:
            return True
        else:
            return False

    if outside_mode:
        if n <= 1 or n >= 10:
            return True
        else:
            return False


def near_ten(num):
    if num % 10 <= 2 or num % 10 == 8 or num % 10 == 9:
        return True
    else:
        return False
