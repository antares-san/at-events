from utils import calc


segment_a = float(input('Введите длину отрезка a: '))
segment_b = float(input('Введите длину отрезка b: '))
segment_c = float(input('Введите длину отрезка c: '))

if calc.is_triangle(a = segment_a, b = segment_b, c = segment_c):
    print('Треугольник cуществует')
else:
    print('Треугольник не cуществует')