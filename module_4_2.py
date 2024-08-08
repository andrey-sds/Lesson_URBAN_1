# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function(val):
    # global pr_  # изменение значения глобальной переменной pr_
    pr_ = "Я в функции test_function"
    # print(f'{pr_} - начальное значение')  # для nonlocal

    def inner_function(val):
        # nonlocal pr_ # изменение значения переменной в функции test_function
        pr_ = "Я в области видимости функции test_function"
        # print(f'{pr_} - переопределение') # nonlocal
        print(pr_)

    inner_function(pr_)
    return pr_


pr_ = "Пример работы пространства имен."
print(f'{pr_} - начало')
print(f'Вызов основной функции: {test_function(pr_)}')
print(f'{pr_} - конец')
print(f'Некорректный вызов вложенной функции inner_function: {inner_function()}')
