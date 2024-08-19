class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_floors:
            print(f'Такого этажа "{new_floor}" не существует в "{self.name}"!')
        else:
            for i in range(new_floor + 1):
                if i > 0:
                    print(f'Этаж: {i}')
                continue


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(int(input(f'Введите нужный этаж для {h1.name}:')))
h2.go_to(int(input(f'Введите нужный этаж для {h2.name}:')))
