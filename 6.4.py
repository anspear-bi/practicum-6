# -*- coding: utf-8 -*-
"""
6.4
"""
position = input("Введите позицию шахматной клетки: ")

def color(position):
    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return "белый" if (column + row) % 2 == 0 else "черный"

print(color(position))


