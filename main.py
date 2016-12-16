from output_functions import *


# 17.70
def one_dimensional_function(x, derivative_order=0):
    return {
        0: math.sqrt(1 + x ** 2) + math.exp(-2 * x),
        1: x / math.sqrt(x ** 2 + 1) - 2 * math.exp(-2 * x),
        2: (-(x ** 2) / ((x ** 2 + 1) ** (3 / 2)) +
            1 / math.sqrt(x ** 2 + 1) + 4 * math.exp(-2 * x))
    }.get(derivative_order,
          ValueError('Введен недопустимый порядок производной.'))


# 17.143
def multidimensional_function(arguments, gradient=False, hessian=False):
    if not (gradient or hessian):
        return 3 * arguments[0] ** 2 + 5 * arguments[1] ** 2 + 4 * arguments[2] ** 2 + 2 * arguments[0] * arguments[1] - arguments[0] * arguments[2] - arguments[1] * arguments[2] + 7 * arguments[0] + arguments[2]
    elif gradient:
        return [6 * arguments[0] + 2 * arguments[1] - arguments[2] + 7,
                10 * arguments[1] + 2 * arguments[0] - arguments[2], 8 * arguments[2] - arguments[0] - arguments[1] + 1]
    else:
        return [[6, 2,  -1],
                [2, 10, -1],
                [-1, -1, 8]]


if __name__ == '__main__':
    print_one_dimensional_methods_tests(0, 1, one_dimensional_function)
    print()
    print_multidimensional_methods_tests(multidimensional_function, 3)
