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
