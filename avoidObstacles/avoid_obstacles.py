def avoid_obstacles(array):
    array = sorted(array)
    max_num = max(array)

    for i in range(1,max_num+1):
        temp_array = []
        for element in array:
            # add each element % i to the array
            temp_array.append(element%i)
        # check if all the items added to the array != 0
        if all(temp_array):
            return i
print(avoid_obstacles([5, 3, 6, 7, 9]))
print(avoid_obstacles([2, 4, 5, 7, 8 ,10, 11]))
