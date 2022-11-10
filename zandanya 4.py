
def reverse_list(lst):
    fst = []
    for i_count in range(len(lst), 0, -1):
        fst.append(i_count)
    return fst

list = [1, 2, 3 , 4]
print(reverse_list(list))