import numpy as np

arr_defualt = np.array([1, 2, 3, 4, 5])
arr_finsh = np.array([])

for i_count in range(0, len(arr_defualt), 1):
    if i_count + 1 != len(arr_defualt):
        arr_finsh = np.append(arr_finsh, arr_defualt[i_count])
        arr_finsh = np.append(arr_finsh, [0]*3)
    else:
        arr_finsh = np.append(arr_finsh, arr_defualt[i_count])


print(arr_finsh)

