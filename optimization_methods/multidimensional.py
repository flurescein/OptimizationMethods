import numpy as np

from math import fabs, floor
from random import uniform


def coordinate_descent(f, arguments_count):
    """Метод покоординатного спуска."""
    a = -100
    b = 100
    e = 0.01

    iterations_count = 0

    def fixed_passive_search(arguments, not_fixed_argument):
        k = floor((b - a) / e)
        x = a

        arg = arguments
        arg[not_fixed_argument] = x
        next_arg = arguments.copy()

        for i in range(0, k + 1):
            next_x = a + (b - a) / k * i
            next_arg[not_fixed_argument] = next_x

            if f(arg) < f(next_arg):
                return arg

            x = next_x
            arg[not_fixed_argument] = x

        next_arg[not_fixed_argument] = b
        if f(arg) > f(next_arg):
            return arg
        else:
            return next_arg

    fixed_values = [0 for x in range(arguments_count)]
    prev_fixed_values = fixed_values.copy()
    while True:
        iterations_count += 1

        for not_fixed_value in range(arguments_count):
            fixed_values = fixed_passive_search(fixed_values, not_fixed_value)

        if (fabs(f(fixed_values) - f(prev_fixed_values)) <= e and
                    np.linalg.norm(np.array(fixed_values).transpose() - np.array(prev_fixed_values).transpose()) <= e):
            break

        prev_fixed_values = fixed_values.copy()

    return [fixed_values, iterations_count]


def gradient_method(f, arguments_count):
    """Градиентный метод."""
    # Случайный выбор e и a. В некоторых случаях
    # дает количество итераций > 20 000
    # e = uniform(0, 1)
    # a = uniform(0.01, 100)
    e = 0.01
    a = 0.12

    x = [1 for x in range(arguments_count)]

    iterations_count = 0

    while np.linalg.norm(np.array(f(x, gradient=True))) > 0.001:
        iterations_count += 1

        if f((np.array(x) - a * np.array(f(x, gradient=True))).tolist()) - f(x) > -a * e * np.linalg.norm(
                np.array(f(x, gradient=True))) ** 2:
            a = uniform(0, 1)

        x = (np.array(x) - a * np.array(f(x, gradient=True))).tolist()

    return [x, iterations_count]


def fletcher_reeves(f, arguments_count):
    """Метод Флетчера-Ривза"""
    def get_a(xk, dk):
        def frange(left_border, right_border, jump):
            while left_border < right_border:
                yield left_border
                left_border += jump

        min_a = -100
        for a in frange(-100, 100, 0.1):
            if f((np.array(xk) + a * np.array(dk)).tolist()) < f((np.array(xk) + min_a * np.array(dk)).tolist()):
                min_a = a
        return min_a

    x = [1 for x in range(arguments_count)]
    d = (-np.array(f(x, gradient=True))).tolist()
    k = 0

    iterations_count = 0

    while np.linalg.norm(np.array(f(x, gradient=True))) > 0.001:
        iterations_count += 1

        a = get_a(x, d)

        if not (k + 1) % arguments_count:
            x = (np.array(x) + a * np.array(d)).tolist()
            d = (-np.array(f(x, gradient=True))).tolist()

        x_prev = x.copy()
        x = (np.array(x) + a * np.array(d)).tolist()
        b = np.linalg.norm(np.array(f(x, gradient=True))) ** 2 / np.linalg.norm(np.array(f(x_prev, gradient=True))) ** 2
        d = (-np.array(f(x, gradient=True)) + b * np.array(d)).tolist()

        k += 1

    return [x, iterations_count]


def steepest_gradient_descent(f, arguments_count):
    """Метод наискорейшего градиентного спуска."""
    def get_a(x):
        def frange(left_border, right_border, jump):
            while left_border < right_border:
                yield left_border
                left_border += jump

        min_a = 0.1
        for a in frange(0.1, 100, 0.1):
            if f((np.array(x) - a * np.array(f(x , gradient=True))).tolist()) < f((np.array(x) - min_a * np.array(f(x , gradient=True))).tolist()):
                min_a = a
        return min_a

    x = [1 for x in range(arguments_count)]
    e = 0.001

    iterations_count = 0

    while np.linalg.norm(np.array(f(x, gradient=True))) > e:
        iterations_count += 1
        x = np.array(x) - get_a(x) * np.array(f(x, gradient=True))

    return [x, iterations_count]


def ravine(f, arguments_count):
    """Овражный метод."""
    def frange(left_border, right_border, jump):
        while left_border < right_border:
            yield left_border
            left_border += jump

    def get_a(x):

        min_a = 0.1
        for a in frange(0.1, 100, 0.1):
            if f((np.array(x) - a * np.array(f(x , gradient=True))).tolist()) < f((np.array(x) - min_a * np.array(f(x , gradient=True))).tolist()):
                min_a = a
        return min_a

    def get_gradient_step(x):
        return np.array(x) - get_a(x) * np.array(f(x, gradient=True))

    def get_ravine_a(y, approximate_y):
        min_a = -100
        for a in frange(-100, 100, 0.1):
            if f((np.array(y) + a * (np.array(approximate_y) - np.array(y))).tolist()) < f((np.array(y) + min_a * (np.array(approximate_y) - np.array(y))).tolist()):
                min_a = a
        return min_a

    x = [1 for x in range(arguments_count)]
    e = 0.001

    iterations_count = 0

    while np.linalg.norm(np.array(f(x, gradient=True))) > e:
        iterations_count += 1

        approximate_x = [num + 0.1 for num in x]

        y = get_gradient_step(x)
        approximate_y = get_gradient_step(approximate_x)

        a = get_ravine_a(y, approximate_y)

        x = [y[num] + (approximate_y[num] - y[num]) * a for num in range(arguments_count)]

    return [x, iterations_count]


def newton(f, arguments_count):
    """Метод Ньютона."""
    x = [1 for x in range(arguments_count)]
    iterations_count = 0

    while np.linalg.norm(np.array(f(x, gradient=True))) > 0.001:
        iterations_count += 1
        x = (np.array(x) - np.dot(np.linalg.inv(np.array(f(x, hessian=True))), np.array(f(x, gradient=True)))).tolist()

    return [x, iterations_count]
