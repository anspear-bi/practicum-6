# -*- coding: utf-8 -*-
"""
6.2
"""
A, B = map(int, input("Введите размеры отверстия: ").split())
C, D, E = map(int, input("Введите размеры кирпича: ").split())


if (C <= A and D <= B) or (D <= A and C <= B) or (E <= A and D <= B) or (D <= A and E <= B):
    print("да")
else:
    print("нет")
