class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        return self.distance

    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name


# if __name__ == '__main__':
#     first = Runner('Вася')
#     second = Runner('Илья')
#
#     print(first.run())
#     print(second.walk())

