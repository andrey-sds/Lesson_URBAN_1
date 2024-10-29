def introspection_info(obj):
    obj_type = type(obj).__name__

    # Получаем все атрибуты и методы объекта
    all_attributes = dir(obj)

    # Отделяем методы от атрибутов
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', 'built-in')

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.name} мне {self.age} лет."


person = Person(input('Введите имя: '), input('Введите возраст:'))

# Используем функцию introspection_info для получения информации об объекте
person_info = introspection_info(person)
print(person_info)
