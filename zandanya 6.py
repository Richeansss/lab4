arr_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_new = []

for i_count in range(0, len(arr_x), 1):
    if arr_x[i_count]  % 2 == 0:
        arr_new.append(i_count)
    else:
        arr_new.append(len(arr_x) - i_count)

print(arr_x)
print(arr_new)