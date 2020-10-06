# difficulty = 8
def array_previous_less(items):
    less_than_list = []

    for i in reversed(range(len(items))):
        for j in reversed(range(i+1)):
            if items[i] > items[j]:
                less_than_list.insert(0,items[j])
                break
            # we go through the list and if none of them 
            # is greater than item[i]
            # then isnert -1 on index 0 
            elif j == 0:
                less_than_list.insert(0,-1)

    return less_than_list

print(array_previous_less([3,5,2,4,5]))