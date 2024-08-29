# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.
class Animal:
    fed = False
    alive = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def eat(self, food):
        if food.edible:
            self.fed = True
            self.alive = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p3 = Fruit('Пьяная вишня')

print(a1.name)
print(p1.name)

print(f'Живой: {a1.alive}')
print(f'Сытый: {a2.fed}')
a1.eat(p1)
a2.eat(p2)

print(f'Живой {a1}: {a1.alive}')
print(f'Сытый {a2}: {a2.fed}')
a1.eat(p3)
print(f'Сытый {a1}: {a1.fed}')
print(f'Живой {a1}: {a1.alive}')
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
