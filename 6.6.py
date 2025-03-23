# -*- coding: utf-8 -*-
"""
6.6
"""
n = int(input("Введите количество детей: "))
k = int(input("Введите количество мест на карусели: "))
m = int(input("Введите время одного сеанса: "))
def time(N, K, M):
    
    rounds = (2 * n + k - 1) // k
    return rounds * m

print(time(N, K, M))
