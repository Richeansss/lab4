import numpy as np

def the_bigest_numb(arr_default):
    print("Изначальный массив", "\n", arr_default, "\n")
    i_unique, i_counts = np.unique(arr_default, return_counts=True)
    i_new_counts = np.sort(i_counts, kind='stable')
    for i_con in range(0, len(i_counts), 1):
        if i_counts[i_con] == i_new_counts[len(i_new_counts)-1]:
            i_need = i_con
    print("Число:", i_unique[i_need], "Встречается кол-во раз:", i_new_counts[len(i_new_counts)-1])
    print("-----------------------------------------------------", "\n")
    return i_unique[i_need], i_new_counts[len(i_new_counts)-1]





arr_x = np.array([1, 1, 1, 1, 1, 2, 2, 2, 5, 24, 24, 24, 24, 24, 24, 1, 1])
arr_y = np.array([2, 3, 5, 3, 1, 2, 2, 2])
arr_z = np.array([24, 24, 24, 24, 24, 24, 1, 1])
the_bigest_numb(arr_x)
the_bigest_numb(arr_y)
the_bigest_numb(arr_z)