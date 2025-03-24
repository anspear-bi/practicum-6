# -*- coding: utf-8 -*-
"""
6.8
"""
def digit_at_position(position):
    digits = ['0'] + [str(i) for i in range(1, 201)]
    return digits[position]

position = int(input("Введите порядковый номер: "))
if 0 <= position <= 201:
    print(digit_at_position(position))
else:
    print("Неправильный номер")
