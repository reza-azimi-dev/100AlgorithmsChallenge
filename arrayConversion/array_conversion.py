def array_conversion(array):
    is_odd = True
    while len(array) != 1:
        array = sum_products(array, is_odd)
        is_odd = not is_odd
    return array[0]

def sum_products(nums, is_odd):
    sum_products = []
    if is_odd:
        for i in range(0,len(nums),2):
            sum_products.append(nums[i] + nums[i+1])
    else:
        for i in range(0,len(nums),2):
            sum_products.append(nums[i] * nums[i+1])
    return sum_products


print(array_conversion([1, 2, 3, 4, 5, 6, 7, 8]))

