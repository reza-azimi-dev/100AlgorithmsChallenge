def array_replace(array, elem_to_replace, sub_elem):
    for item in range(len(array)):
        if array[item] == elem_to_replace:
            array[item] = sub_elem
    return array

print(array_replace([1,2,1,1,1,1,1,3,4,1], 1, 3))