def array_change(array):
    moves = 0
    for item in range(len(array)-1):
        while array[item] >= array[item +1]:
            array[item+1] += 1
            moves += 1
    return [array,moves]

print(array_change([1, 1, 1]))
print(array_change([1, 2, 1]))
print(array_change([3,1,1,2]))