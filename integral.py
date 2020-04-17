import numpy as np
import math


def rectangle_func(func, low_lim, high_lim, delta):
    def integration_exe_func(func, low_lim, high_lim, n):
        integral = 0.0
        step = (high_lim - low_lim) / n
        for x in np.arange(low_lim, high_lim - step, step):
            integral += step * func(x + step / 2)
        return integral

    sigma, n = 1, 1
    while math.fabs(sigma) > delta:
        sigma = (integration_exe_func(func, low_lim, high_lim, n * 2) - integration_exe_func(func, low_lim, high_lim, n)) / 3        # правило Рунге Δ2n ≈ |I2n - In|
        n *= 2

    result = math.fabs(integration_exe_func(func, low_lim, high_lim, n))
    sigma_result = result + sigma
    if result > sigma_result:
        result, sigma_result = sigma_result, result
    print("------------------------------------------------")
    print('Метод прямокутників:')
    print(f'Здійснено розбиттів: {n}')
    print(f'Результат: {result}')
    print(f'Результат з урахуванням похибки: {sigma_result}')


def trapeze_func(func, low_lim, high_lim, delta):
    def integration_exe_func(func, low_lim, high_lim, n):
        integral = 0.0
        step = (high_lim - low_lim) / n
        for x in np.arange(low_lim, high_lim - step, step):
            integral += step * (func(x) + func(x + step)) / 2
        return integral

    sigma, n = 1, 1
    while math.fabs(sigma) > delta:
        sigma = (integration_exe_func(func, low_lim, high_lim, n * 2) - integration_exe_func(func, low_lim, high_lim, n)) / 3
        n *= 2

    result = math.fabs(integration_exe_func(func, low_lim, high_lim, n))
    sigma_result = result + sigma
    if result > sigma_result:
        result, sigma_result = sigma_result, result
    print("------------------------------------------------")
    print('Метод середніх трапецій:')
    print(f'Здійснено розбиттів: {n}')
    print(f'Результат: {result}')
    print(f'Результат з урахуванням похибки: {sigma_result}')

def simpson_func(func, low_lim, high_lim, delta):
    def integration_exe_func(func, low_lim, high_lim, n):
        integral = 0.0
        step = (high_lim - low_lim) / n
        for x in np.arange(low_lim + step / 2, high_lim - step / 2, step):
            integral += step / 6 * (func(x - step / 2) + 4 * func(x) + func(x + step / 2))
        return integral

    sigma, n = 1, 1
    while math.fabs(sigma) > delta:
        sigma = (integration_exe_func(func, low_lim, high_lim, n * 2) - integration_exe_func(func, low_lim, high_lim, n)) / 15
        n *= 2

    result = math.fabs(integration_exe_func(func, low_lim, high_lim, n))
    sigma_result = result + sigma
    if result > sigma_result:
        result, sigma_result = sigma_result, result
    print("------------------------------------------------")
    print('Метод парабол (Сімпсона):')
    print(f'Здійснено розбиттів: {n}')
    print(f'Результат: {result}')
    print(f'Результат з урахуванням похибки: {sigma_result}')


rectangle_func(lambda x: (x * math.e ** x) / (1 + x) ** 2, low_lim=0.0, high_lim=1.0, delta=0.001)
trapeze_func(lambda x: x / (1 + x), low_lim=0.0, high_lim=1.0, delta=0.001)
simpson_func(lambda x: 2 * x / (1 + x ** 2), low_lim=0.0, high_lim=2.0, delta=0.001)
