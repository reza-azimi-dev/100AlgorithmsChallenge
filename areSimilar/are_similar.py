def are_similar(a,b):

# Faster way using python:
#    if sorted(a) == sorted (b):
#        return True

# The Cooler Way

    if a == b:
        return True
    else:
        c= []
        d= []
        for item in range(len(a)):
            if a[item] != b[item]:
                c.append(a[item])
                d.append(b[item])
        d.reverse()
        return len(c) == 2 and d == c


    
    




print(are_similar([1, 2, 3], [1, 2, 3]))
print(are_similar([1, 2, 3], [2, 1, 3]))
print(are_similar([1, 2, 2], [2, 1, 1]))
