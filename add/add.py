def add(param1, param2):
    return param1 + param2

def add2(*parameters):
    total = 0
    for item in parameters:
        total += item
    return total

print(add(1, 2))
print(add(3, 2))

print(add2(1,2,3,4,5))
print(add2(2,3))