from utils import calc


title = "Введите значение координаты x для точки"
point_a = float(input(f'{title} А: '))
point_b = float(input(f'{title} B: '))

# Использование позиционных аргументов
print(f'Длина отрезка {calc.segment_len(point_a, point_b)}')
