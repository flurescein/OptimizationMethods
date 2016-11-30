import math


def passive_search(a, b, f):
    """Пассивный поиск."""
    e = 0.001
    k = math.floor((b - a) / e)

    x = a

    for i in range(0, k + 1):
        next_x = a + (b - a) / k * i

        if f(x) < f(next_x):
            return x

        x = next_x

    if f(x) < f(b):
        return x
    else:
        return b


def dichotomy(a, b, f):
    """Метод дихотомии."""
    delta = 0.1
    e = 0.001
    c = 0
    d = 0

    while b - a > 2 * e:
        c = (b + a) / 2 - delta
        d = (b + a) / 2 + delta

        if f(c) < f(d):
            b = c
        else:
            a = d

    return (d + c) / 2


def golden_ratio(a, b, f):
    """Метод золотого сечения."""
    e = 0.001

    new_a = a
    new_b = b

    c = (3 - math.sqrt(5)) / 2 * (b - a) + a
    d = (math.sqrt(5) - 1) / 2 * (b - a) + a

    while (new_b - new_a) / 2 > e:
        if f(c) <= f(d):
            new_b = d
            d = c
            c = (3 - math.sqrt(5)) / 2 * (new_b - new_a) + new_a
        else:
            new_a = c
            c = d
            d = (math.sqrt(5) - 1) / 2 * (new_b - new_a) + new_a

    return (new_b + new_a) / 2


def fibonacci_search(a, b, f):
    """Метод Фибоначчи."""
    def get_fibonacci_number(n):
        if n == 1 or n == 2:
            return 1
        else:
            return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)

    x = 1
    i = 0
    delta = 0.1
    e = 0.1

    while get_fibonacci_number(x) <= b - a / e:
        x += 1

    while x != 1:
        i += 1
        c = a + (b - a) * get_fibonacci_number(x + 1) / get_fibonacci_number(x + 3)
        d = a + (b - a) * get_fibonacci_number(x + 2) / get_fibonacci_number(x + 3)

        if c == d:
            c = a + (b - a) * get_fibonacci_number(x + 1) / get_fibonacci_number(x + 3) + delta
            d = a + (b - a) * get_fibonacci_number(x + 2) / get_fibonacci_number(x + 3) - delta
        if f(c) < f(d):
            b = c
        else:
            a = d

        x -= 1

    return (b + a) / 2


def tangents(a, b, f):
    """Метод касательных."""

    def get_c(left_dot, right_dot):
        """Находит точку пересечения касательных."""
        return ((f(left_dot) - f(left_dot, 1) * left_dot - f(right_dot) + f(right_dot, 1) * right_dot) /
                (f(right_dot, 1) - f(left_dot, 1)))

    e = 0.01
    left_dot = a
    right_dot = b
    c = get_c(left_dot, right_dot)

    while (math.fabs(right_dot - left_dot) > e and
           math.fabs(f(c, 1)) > e and
           math.fabs(f(right_dot) - f(left_dot)) > e):
        if f(c, 1) > 0:
            right_dot = c
        else:
            if f(c, 1) < 0:
                left_dot = c
            else:
                return c

    return (right_dot + left_dot) / 2


def newton_raphson(a, b, f):
    e = 0.001
    x = a
    while math.fabs(f(x, 1)) > e:
        x -= f(x, 1) / f(x, 2)

    return x


def secants(a, b, f):
    e = 0.001
    prev_x = a
    x = a + e
    while math.fabs(f(x, 1)) > e:
        tmp = x
        x -= (x - prev_x) / (f(x, 1) - f(prev_x, 1)) * f(x, 1)
        prev_x = tmp

    return x
