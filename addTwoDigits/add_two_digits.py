def add_two_digits(number):

    digits = []
    for item in str(number):
        digits.append(int(item))
    return sum(digits)
    
print(add_two_digits(464645))