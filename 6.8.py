# -*- coding: utf-8 -*-
"""
6.8
"""

x1,y1 = map(int(input('Введите координаты центра 1 окружности: ')).split())
r1 =  int (input('Введите радиус 1 окружности: '))
x2,y2 = map(int(input('Введите координаты центра 2 окружности: ')).split())
r2 =  int (input('Введите радиус 2 окружности: '))
def position (x1, y1, r1, x2, y2, r2):
    distance_squared = (x1 - x2) * 2 + (y1 - y2) * 2
    r1_r2_sum_squared = (r1 + r2) * 2
    r1_r2_diff_squared = (r1 - r2) * 2

    if distance_squared > r1_r2_sum_squared:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance_squared == r1_r2_sum_squared:
        return "Окружности имеют внешнее касание"
    elif r1_r2_diff_squared < distance_squared < r1_r2_sum_squared:
        return "Окружности пересекаются"
    elif distance_squared == r1_r2_diff_squared:
        return "Окружности имеют внутреннее касание"
    else:
        return "Одна окружность лежит внутри другой, не касаясь"

print(position(x1, y1, r1, x2, y2, r2))