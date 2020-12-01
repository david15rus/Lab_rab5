#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента списка;
# 2) сумму модулей элементов списка, расположенных после первого отрицательного элемента.

import sys

N = 10
if __name__ == '__main__':
    A = list(map(float, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Выполняется 1 часть задания(нахождение минимальноего по модулю числа)
    a_min = A[0]
    i_min = 0
    for i, item in enumerate(A):
        if item < abs(a_min):
            i_min, a_min = i, item
    print('Минимальное по модулю число: ', a_min)

    # Выполнение 2 части задание (нахождение суммы модулей чисел после 1 отрицательного)
    neg = -1
    for i, item in enumerate(A, 1):
        if item < 0:
            neg = i
            break

    if neg == -1:
        print('Отрицательных нет')

    else:
        print('Номер первого отриц.:', neg)
        s = 0
        for i in range(neg, len(A)):
            s += abs(A[i])

        print('Сумма модулей: ', s)
