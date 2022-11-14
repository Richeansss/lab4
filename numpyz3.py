import numpy as np

a = np.random.randint(0, 1000, [3, 5])
print('Исходный массив:')
print(a, "\n")

print('Средние значения каждой строки матрицы')
print(a.mean(axis=1), "\n")

a = a - a.mean(axis=1, keepdims=True)
print('вычитание из матрицы средних значений')
print(a)
