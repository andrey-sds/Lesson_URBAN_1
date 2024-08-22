# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
# возвращать результаты сравнения по соответствующим операторам.
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
class House:

    def __init__(self, name, number_of_floors: int):
        self.name = name

        self.number_of_floors = number_of_floors

    def __len__(self):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors
        else:
            print('Значение не является числом, возвращаем 0')
            return 0

    def __str__(self):
        return f'Название: {self.name}; количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, (House, int)):
            print("Значения должны быть типом int")
        return self.number_of_floors == other

    def __lt__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
        return self.number_of_floors < other

    def __le__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
        return self.number_of_floors <= other

    def __gt__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
            return False
        return self.number_of_floors > other

    def __ge__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
            return False
        return self.number_of_floors >= other

    def __ne__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
            return False
        return self.number_of_floors != other

    def __add__(self, other):
        if not isinstance(other, (int, House)) or not isinstance(self.number_of_floors, (int, House)):
            print("Значения должны быть типом int")
            return 0
        self.number_of_floors = self.number_of_floors + other
        return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, House)):
            print("Значения должны быть типом int")
            return other
        sc = other if isinstance(other, int) else other.number_of_floors
        self.number_of_floors += sc

        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(f'{h1 == h2} метод eq')

h1 = h1 + 10  # __add__
print(f'{h1} - метод add')
print(f'{h1 == h2} метод eq, после отработки метода add')

h1 += 10  # __iadd__
print(f'{h1} - метод iadd')

h2 = 10 + h2  # __radd__
print(f'{h2} - метод radd')

print(f'{h1 > h2} - метод gt')
print(f'{h1 >= h2} - метод ge')
print(f'{h1 < h2} - метод lt')
print(f'{h1 <= h2} - метод le')
print(f'{h1 != h2} - метод ne')
