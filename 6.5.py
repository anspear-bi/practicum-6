# -*- coding: utf-8 -*-
"""
6.5
"""

def good(begin, end):
    begin_x = ord(begin[0]) - ord('a')
    begin_y = int(begin[1]) - 1
    end_x = ord(end[0]) - ord('a')
    end_y = int(end[1]) - 1

    dx = abs(begin_x - end_x)
    dy = abs(begin_y - end_y)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

move = input("Введите ход: ")
begin, end = map(input('Введите ход (через дефис): ').split('-'))
if good(begin, end):
    print("Верно")
else:
    print("Ошибка")
