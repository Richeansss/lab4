import numpy as np

def the_larges_values(arr_default):
    print("Изначальный массив", "\n", arr_default, "\n")
    i_unique, i_counts = np.unique(arr_default, return_counts=True)
    arr_mass = np.concatenate((i_unique, i_counts), axis = 0).reshape((2, 9))
    num_rows, num_cols = arr_mass.shape
    for i_j in range(0, num_cols-1):
        for i_c in range(0, num_cols-1):
            if (arr_mass[1, i_c] > arr_mass[1, i_c + 1]):
                i_tmp =  arr_mass[1, i_c]
                arr_mass[1, i_c] = arr_mass[1, i_c + 1]
                arr_mass[1, i_c + 1] = i_tmp
                i_tmp = arr_mass[0, i_c]
                arr_mass[0, i_c] = arr_mass[0, i_c + 1]
                arr_mass[0, i_c + 1] = i_tmp
    print(arr_mass)
    print("Введите кол-во желаемых частво встречающихся знайчений не больше", num_cols)
    i_numb = int(input())
    print("Числа", "\n", arr_mass[:,i_numb-1:], "\n", "Встречаются")

arr_random = np.random.randint(0,9,(10,10))

the_larges_values(arr_random)


