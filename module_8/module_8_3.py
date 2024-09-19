class Car():
    def __init__(self, model, __vin, __numbers):
        self.model = model
        __vin = self.__is_valid_vin(__vin)
        __numbers = self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999:
            return True
        elif not isinstance(vin_number, int):
            raise IncorrectCarNumbers(f'Некорректный тип данных для vin номера - {vin_number}')
        else:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера - {vin_number}')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        elif not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров - {numbers}')
        else:
            raise IncorrectCarNumbers(f'Неверная длина номера - {numbers}')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
