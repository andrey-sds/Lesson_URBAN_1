from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'Name: {self.name}, weight: {self.weight}, category: {self.category}'


class Shop:

    def get_products(self):
        self.__file_name = '../products.txt'
        file = open(self.__file_name, 'r', encoding='utf-8')
        products = [file.read()]
        file.close()
        return f'{products}'

    def add(self, *products):
        current_products = self.get_products()
        # pprint(current_products)

        file = open(self.__file_name, 'a', encoding='utf-8')

        for product in products:
            if str(product) in current_products:
                print(f'{product} уже есть в файле!')
            else:
                file.write(f'{product}\n')
                print(f'{product} добавлен в файл!')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
