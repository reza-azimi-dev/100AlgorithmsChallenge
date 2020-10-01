def alphabet_sub_sequence(s): 

    char_values = [ord(i) for i in list(s)]
    char_values_set = set(char_values)

    if len(char_values) != len(char_values_set):
        return False
    for i in range(len(char_values)-1):
        if char_values[i] >= char_values[i+1]:
            
            return False
    return True
    
print(alphabet_sub_sequence('zab'))
print(alphabet_sub_sequence('effg'))
print(alphabet_sub_sequence('cdce'))
print(alphabet_sub_sequence('ace'))
print(alphabet_sub_sequence('bxz'))
