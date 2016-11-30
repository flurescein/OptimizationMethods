from optimization_methods.one_dimensional import *
import math
import time


def print_method_test(a, b, f, method, method_name):
    """Выводит результат и время работы метода."""
    start_time = time.time()
    result = round(method(a, b, f), 2)
    end_time = time.time()

    print(method_name, '\t', result, '\t', end_time - start_time)


def print_methods_tests(a, b, f):
    """Выводит результат и время работы всех методов."""
    print('Method name\t', 'Result\t', 'Time')
    print_method_test(a, b, f, passive_search, 'Passive')
    print_method_test(a, b, f, dichotomy, 'Dichotomy')
    print_method_test(a, b, f, golden_ratio, 'Golden r..')
    print_method_test(a, b, f, fibonacci_search, 'Fibonacci')
    print_method_test(a, b, f, tangents, 'Tangents')
    print_method_test(a, b, f, newton_raphson, 'New-Rap')
    print_method_test(a, b, f, secants, 'Secants')


def function(x, derivative_order=0):
    return {
        0: math.sqrt(1 + x ** 2) + math.exp(-2 * x),
        1: x / math.sqrt(x ** 2 + 1) - 2 * math.exp(-2 * x),
        2: (-(x ** 2) / ((x ** 2 + 1) ** (3 / 2)) +
            1 / math.sqrt(x ** 2 + 1) + 4 * math.exp(-2 * x))
    }.get(derivative_order,
          ValueError('Введен недопустимый порядок производной.'))

if __name__ == '__main__':
    print_methods_tests(0, 1, function)
