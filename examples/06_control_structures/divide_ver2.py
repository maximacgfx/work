# -*- coding: utf-8 -*-

try:
    a = input('Введите строку : ')
    b = input('Введите вторую строку: ')
    print('Результат: ', str (a) / str(b))
except (ValueError, ZeroDivisionError, TypeError):
    print('Что-то пошло не так...')
'''
Example:

$ python divide_ver2.py
Введите первое число: wer
Введите второе число: 4
Результат:  Что-то пошло не так...

$ python divide_ver2.py
Введите первое число: 5
Введите второе число: 0
Результат:  Что-то пошло не так...
'''
