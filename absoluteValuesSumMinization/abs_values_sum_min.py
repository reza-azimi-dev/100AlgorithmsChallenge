import math

def abs_values_sum_min(number):
    #check if the number is even or odd:
    is_even = len(number) % 2 == 0

    if is_even:
        result = number[int((len(number) /2) - 1)] 
    elif not is_even:
        result = number[math.floor(len(number) /2)]
    return result

print(abs_values_sum_min([2, 4, 7]))
print(abs_values_sum_min([2, 4, 7, 6]))
print(abs_values_sum_min([2, 4, 7, 6, 6]))
print(abs_values_sum_min([2, 4, 7, 6, 6, 8]))