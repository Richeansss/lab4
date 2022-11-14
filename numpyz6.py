import numpy as np

def change_rows(arr_default):
    print("Изначальный массив", "\n", arr_default, "\n")
    num_rows, num_cols = arr_default.shape
    arr_default[[0, num_rows-1]] = arr_default[[num_rows-1, 0]]
    print("Итоговый массив", "\n", arr_default, "\n")
    print("------------------------------------------", "\n")
    return arr_default

fst_array = np.random.randint(0, 10, [5, 5])
snd_array = np.random.randint(0, 10, [4, 5])
trd_array = np.random.randint(0, 10, [5, 4])

change_rows(fst_array)
change_rows(snd_array)
change_rows(trd_array)