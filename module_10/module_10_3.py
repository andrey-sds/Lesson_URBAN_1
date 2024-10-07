import threading
from random import randint
from time import sleep


class Bank:
    balance = 0
    lock = threading.Lock()

    def __init__(self):
        pass

    def deposit(self):
        for i in range(100):
            summ = randint(50, 500)
            self.balance += summ
            print(f'Пополнение баланса: {summ}. На счету: {self.balance}\n')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            summ = randint(50, 500)
            print(f'Запрос на снятие: {summ}\n')
            if summ <= self.balance:
                self.balance -= summ
                print(f'Снятие со счета: {summ}. На счету: {self.balance}\n')
            else:
                print(f'Запрос отклонен, недостаточно средств. На счету: {self.balance}\n')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
