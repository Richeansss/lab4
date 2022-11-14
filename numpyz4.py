import numpy as np

def get_massiv(arr_default):
    num_rows, num_cols = arr_default.shape
    print("Изначальный массив", "\n", arr_default, "\n")
    for i_count in range(0, num_rows, 1):
        for j_count in range(0, num_cols, 1):
            if (arr_default[i_count, j_count] >= 3) and (arr_default[i_count, j_count] <= 8):
                arr_default[i_count, j_count] = arr_default[i_count, j_count] * -1
    print("Итоговый массив", "\n", arr_default, "\n")
    print("------------------------------------------", "\n")
    return arr_default

fst_array = np.random.randint(0, 10, [5, 5])
snd_array = np.random.randint(0, 10, [5, 5])
trd_array = np.random.randint(0, 10, [5, 5])

get_massiv(fst_array)
get_massiv(snd_array)
get_massiv(trd_array)