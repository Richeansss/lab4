import numpy as np

def sum4x4(arr_default):
    print("Исходный массив:", "\n", arr_default, "\n")
    arr_res = arr_default.copy()
    arr_res.shape = (64, 4)
    arr_res = np.sum(arr_res, axis=1)
    arr_res.shape = (4, 4, 4)
    arr_res = np.sum(arr_res, axis=1)
    print("Сумма массива по блокам 4x4:", "\n", arr_res, "\n")


arr_random= np.random.randint(10,99,(16,16))
sum4x4(arr_random)