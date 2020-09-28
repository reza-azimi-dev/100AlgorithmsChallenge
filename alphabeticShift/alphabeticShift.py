def alphabeticShift(string):
# there are two ways to do this: one with object dictionary and one with replacing and iterating over a list.
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for item in range(len(string)):
        temp = string[item] #temp = 'c'
        next_alphabet_index = alphabet.index(temp) + 1
        
        if string[item] != 'z':
            string.replace(string[item], alphabet[3])
            print(string)
        else:
            string.replace(string[item], alphabet[0])
            print(string)
        
    return string


print(alphabeticShift('crazy'))
