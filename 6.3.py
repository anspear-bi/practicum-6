# -*- coding: utf-8 -*-
"""
6.3
"""

def foo(N, M, K):
    return K in {i * (M + 1) for i in range(1, N + 1)} or K in {j * (N + 1) for j in range(1, M + 1)}

N, M = map(int, input("Введите размер кварталов: ").split())
K = int(input("Введите K: "))

if foo(N, M, K):
    print("Успешно")
else:
    print("Неосуществимо")




