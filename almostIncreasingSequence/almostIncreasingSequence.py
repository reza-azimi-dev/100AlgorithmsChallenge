def almostIncreasingSequence(numbers):
    
    result = False
    for item in range(len(numbers)-1):
        x=0
        if item > numbers[item+1]:
            x += 1
            if x < 2:
                result = True
            
    return result

print(almostIncreasingSequence([1, 3, 2, 1])) 
print(almostIncreasingSequence([1, 3, 2])) 