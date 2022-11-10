
def more_than_five(lst):
    fst = []
    for i_count in range(1, len(lst), 1):
        if abs(lst[i_count]) > 10:
            fst.append(lst[i_count])
    return fst


slist = [1, 2, 3, 4, -10, -11, 20]
print(more_than_five(slist))