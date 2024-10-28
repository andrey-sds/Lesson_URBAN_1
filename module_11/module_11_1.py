import numpy as np

# 1. Создание массива чисел
array = np.array([1, 2, 3, 4, 5])
print("Исходный массив:", array)

# 2. Выполнение математической операции: сложение
added_array = np.add(array, 10)
print("Массив после добавления 10 к каждому элементу:", added_array)

# 3. Выполнение математической операции: умножение
multiplied_array = np.multiply(array, 2)
print("Массив после умножения каждого элемента на 2:", multiplied_array)

# 4. Вычисление среднего значения массива
mean_value = np.mean(array)
print("Среднее значение массива:", mean_value)

# 5. Транспонирование (для одномерного массива это не меняет массив, но демонстрирует метод)
transposed_array = np.transpose(array)
print("Транспонированный массив:", transposed_array)

# Для демонстрации транспонирования лучше использовать двумерный массив
matrix = np.array([[1, 2, 3], [4, 5, 6]])

transposed_matrix = np.transpose(matrix)
print("Исходная матрица:\n", matrix)
print(f"Количество элементов массива: {matrix.size}")
print("Транспонированная матрица:\n", transposed_matrix)
