from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

        print(f'{self.name}, на нас напали!')

    def run(self):
        res = self.enemy
        i = 0
        while res > 0:
            res -= self.power
            i += 1
            print(f'{self.name} сражается {i} дней, осталось воинов {res}')
            sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {i} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
