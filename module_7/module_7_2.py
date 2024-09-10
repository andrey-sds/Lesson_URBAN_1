# Создайте функцию custom_write(file_name, strings), которая принимает аргументы
# file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell()
# перед записью.

from pprint import pprint


def custom_write(file_name, strings):
    # Открываем файл для записи, чтобы при запуске очищался
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    # счетчик строк в файле
    i = 0
    for str_ in strings:
        i += 1
        # добавляем значения в словарик
        strings_positions.update({(i, file.tell()): str_})
        file.write(str_ + '\n')
    # закрываем файл
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
   print(elem)
