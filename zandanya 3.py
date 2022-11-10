
def is_prime(i_numb):
    i_prost = 0
    if (i_numb >= 0) and (i_numb <= 1000):
        i_range = i_numb // 2 + 1
        for i in range(2, i_range):
            if (i_numb % i == 0):
                i_prost = i_prost + 1
            if (i_prost <= 0):
                return True
            else:
                return False
    else:
        return 'Число не входит в диапозон от 0 до 1000'


print(is_prime(5))