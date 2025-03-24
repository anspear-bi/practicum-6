# -*- coding: utf-8 -*-
"""
6.6
"""
N = int(input("Введите количество детей: "))
K = int(input("Введите количество мест на карусели: "))
M = int(input("Введите время одного сеанса: "))
def time(self, N, K, M):

    
    rounds = (2 * N + K - 1) // K
    return rounds * M

print(time(N, K, M))
