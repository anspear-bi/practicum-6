# -*- coding: utf-8 -*-
"""
6.1
"""
import math
r = 6.5
A,B = map (int,input('Введите размеры покрытия: ').split())

def carpet(r, A, B):
    if math.sqrt(A ** 2 + B ** 2) < r*2:
        return "да"
    else:
        return "нет"


print(carpet(r, A, B))