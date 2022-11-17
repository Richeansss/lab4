import numpy as np

def arr_10x3equiltrue(arr_default):
    print("Исходный массив:", "\n", arr_default, "\n")
    f_logic = np.logical_and.reduce(arr_default[:,1:] == arr_default[:,:-1], axis=1)
    arr_equil0 = arr_default[~f_logic]
    print("Неравные строки в массиве:", "\n", arr_equil0, "\n")
    print("-----------------------------------------------------", "\n")
    return arr_equil0

arr_random1 = np.random.randint(0,2,(10,3))
arr_random2 = np.random.randint(0,2,(10,3))
arr_random3 = np.random.randint(0,2,(10,3))

arr_10x3equiltrue(arr_random1)
arr_10x3equiltrue(arr_random2)
arr_10x3equiltrue(arr_random3)