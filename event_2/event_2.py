from utils import calc
from utils import outfunc


print(calc.__doc__)
print(calc.is_triangle.__doc__)
print(calc.segment_len.__doc__)

# Именнованные аргументы
print('Это треугольник?: ', calc.is_triangle(b = 2, a = 5, c = 6))
print('Длина отрезка = ', calc.segment_len(point_b = 3, point_a = -2))

# Позиционные аргументы
print('Это треугольник? : ', calc.is_triangle(5,2,6))
print('Длина отрезка = ', calc.segment_len(-2, 3))

# Позиционные и именнованные аргументы
print('Это треугольник? : ', calc.is_triangle(5, c = 6, b = 2))

# Использование **kwargs
print(outfunc.format_card('Person card', id ='15343', name ='Daniel', birthday ='16 мая'))

# Использование *args
print(outfunc.format_list('Alice', 'Daniel', 'Maria', title ='Colleagues'))
print(outfunc.format_list('Soup', 'Salad', 'Beverage'))

# lambda examples
double = lambda x: x * 2
print(double(5))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(f'Start list: {my_list}')
print(f'New list: {new_list}')

max_number = lambda a, b: a if a > b else b
print(max_number(3, 5))

tables = [lambda x = x: x * 10 for x in range(1, 11)]
print(type(tables), tables)
for table in tables:
    print(table())  # call lambda function for each element

numbers = []
for x in range(1, 11):
    numbers.append(x)
table = list(map(lambda x: x * 10, numbers))
print(table)    