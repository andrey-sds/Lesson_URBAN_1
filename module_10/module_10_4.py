from queue import Queue
from threading import Thread
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_wait = randint(3, 10)
        sleep(time_to_wait)


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            table_found = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    table_found = True
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            if not table_found:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
