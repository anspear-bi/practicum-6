# -*- coding: utf-8 -*-
"""
6.10
"""
class Rectangle:
    def __init__(self, top: int, left: int, bottom: int, right: int):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def is_inside(self, rectangle: 'Rectangle') -> bool:
        return (self._is_inside_horizontal(rectangle) and
                self._is_inside_vertical(rectangle))

    def is_collision(self, rectangle: 'Rectangle') -> bool:
        return (self._is_horizontal_collision(rectangle) and
                self._is_vertical_collision(rectangle))

    def _is_inside_horizontal(self, rectangle: 'Rectangle') -> bool:
        return self.left >= rectangle.left and self.right <= rectangle.right

    def _is_inside_vertical(self, rectangle: 'Rectangle') -> bool:
        return self.top >= rectangle.top and self.bottom <= rectangle.bottom

    def _is_horizontal_collision(self, rectangle: 'Rectangle') -> bool:
        return not (self.right < rectangle.left or self.left > rectangle.right)

    def _is_vertical_collision(self, rectangle: 'Rectangle') -> bool:
        return not (self.bottom < rectangle.top or self.top > rectangle.bottom)

    def __str__(self):
        return f'Rectangle(top={self.top}, left={self.left}, bottom={self.bottom}, right={self.right})'


coordinates = map(int, input('First rectangle (top left bottom right): ').strip().split())
top, left, bottom, right = coordinates
rectangle1 = Rectangle(top, left, bottom, right)
coordinates = map(int, input('Second rectangle (top left bottom right): ').strip().split())
top, left, bottom, right = coordinates
rectangle2 = Rectangle(top, left, bottom, right)

if rectangle1.is_inside(rectangle2):
    print('First rectangle is inside second')
elif rectangle2.is_inside(rectangle1):
    print('Second rectangle is inside first')
elif rectangle1.is_collision(rectangle2):
    print('First rectangle collisions with second')
else:
    print('Rectangles do not collide')

    