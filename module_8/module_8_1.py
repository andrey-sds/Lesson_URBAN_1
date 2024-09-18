def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exc:
        print(f'Одно из значений не является числом {exc}: a - {type(a)}; b - {type(b)} ')
        return f'Склеиваем a и b как строки: {str(a) + str(b)}'
   
    print(f'Обе переменные - числа a - {type(a)}; b - {type(b)}')
    return f'Сумма чисел: {round(a + b,3)}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
