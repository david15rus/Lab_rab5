#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
   A = list(map(int, input('Введите список ').split()))
   numb = int(input('Введите число, котрое нужно найти в списке '))
   for i in range(len(A)):
      if A[i] == numb:
         index = i
         break
   else:
      print('В списке нет искомого элемента', file=sys.stderr)
      exit(1)
   print('Индекс искомого элемента: ', index)