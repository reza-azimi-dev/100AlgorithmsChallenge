def alternating_sum(array):
    index_even = []
    index_odd = []
    index_counter = 0
    for item in range(len(array)):
        if index_counter % 2 ==0:
            index_even.append(array[item])
            index_counter+=1
        elif index_counter % 2 !=0:
            index_odd.append(array[item])
            index_counter+=1
    print(index_odd)
    print(index_even)
    
    sum_even = 0 
    sum_odd = 0

    for item in index_even:
        sum_even+= item
    for item in index_odd:
        sum_odd+= item
    
    return [sum_even, sum_odd]


print(alternating_sum([50,60,60,45,70]))
