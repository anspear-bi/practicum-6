# -*- coding: utf-8 -*-
"""
6.7
"""
k = int(input("Введите количество суши: "))

def sushi(k):
    for n in range(k // 5 + 1):
        if (k - 5 * n) % 7 == 0:
            return True

if sushi(k):
    print("Можно заказать")
else:
    print("Нельзя заказать")
