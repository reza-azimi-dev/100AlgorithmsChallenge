def adjacentElementsProduct(numbers):
    list_of_products = []
    for item in range(len(numbers) - 1):
        product = numbers[item] * numbers[item + 1]
        list_of_products.append(product)
    return max(list_of_products)

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))