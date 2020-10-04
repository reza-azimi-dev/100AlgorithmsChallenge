def array_maximal_adjacent_difference(array):
    dif = 0
    for i in range(len(array)):
        if i== 0:
            temp_dif = check_adjacent_abs_dif(array[i],array[i+1])
            if temp_dif > dif:
                dif = temp_dif
        elif i == (len(array)-1):
            temp_dif = check_adjacent_abs_dif(array[i],array[i-1])
            if temp_dif > dif:
                dif = temp_dif
        elif i != 0 and i != (len(array)-1):
            dif_from_left = check_adjacent_abs_dif(array[i],array[i-1])
            dif_from_right = check_adjacent_abs_dif(array[i],array[i+1])

            if dif_from_left > dif_from_right and dif_from_left > dif:
                dif = dif_from_left
            else:
                if dif_from_right > dif:
                    dif = dif_from_right
    return dif

def check_adjacent_abs_dif(left,right):
    check_dif = left - right
    return abs(check_dif)

print(array_maximal_adjacent_difference([2,4,1,0,4,6,1,4,13,2,5,5,2,8]))