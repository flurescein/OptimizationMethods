import time

from optimization_methods.one_dimensional import *
from optimization_methods.multidimensional import *

def print_one_dimensional_method_test(a, b, f, method, method_name):
    """Выводит результат и время работы метода."""
    start_time = time.time()
    result = method(a, b, f)
    end_time = time.time()

    result[0] = round(result[0], 2)

    print(method_name, '\t', result[0], '\t', result[1], '\t', end_time - start_time)


def print_multidimensional_method_test(f, arguments_count, method, method_name):
    start_time = time.time()
    result = method(f, arguments_count)
    end_time = time.time()

    iters = result[1]
    result = [round(x, 2) for x in result[0]]

    print(method_name, '\t', result, '\t', iters, '\t', end_time - start_time)


def print_one_dimensional_methods_tests(a, b, f):
    """Выводит результат и время работы всех методов."""
    print('Method name\t', 'Result\t', 'Iters\t', 'Time')
    print_one_dimensional_method_test(a, b, f, passive_search, 'Passive')
    print_one_dimensional_method_test(a, b, f, dichotomy, 'Dichotomy')
    print_one_dimensional_method_test(a, b, f, golden_ratio, 'Golden r..')
    print_one_dimensional_method_test(a, b, f, fibonacci_search, 'Fibonacci')
    print_one_dimensional_method_test(a, b, f, tangents, 'Tangents')
    print_one_dimensional_method_test(a, b, f, newton_raphson, 'New-Rap')
    print_one_dimensional_method_test(a, b, f, secants, 'Secants')


def print_multidimensional_methods_tests(f, arguments_count):
    print('Method name\t', 'Result\t\t\t', 'Iters\t', 'Time')
    print_multidimensional_method_test(f, arguments_count, coordinate_descent, 'Coord. des')
    print_multidimensional_method_test(f, arguments_count, gradient_method, 'Gradient')
    print_multidimensional_method_test(f, arguments_count, steepest_gradient_descent, 'SGDM    ')
    print_multidimensional_method_test(f, arguments_count, ravine, 'Ravine  ')
    print_multidimensional_method_test(f, arguments_count, fletcher_reeves, 'Flet-Reev')
    print_multidimensional_method_test(f, arguments_count, newton, 'Newton   ')