def are_eqally_strong(myLeft,myRight,yourLeft,yourRight):
    if myLeft <= myRight:
        myWeakest = myLeft
        myStrongest = myRight
    else:
        myWeakest = myRight
        myStrongest = myLeft

    if yourLeft <= yourRight:
        yourWeakest = yourLeft
        yourStrongest = yourRight
    else:
        yourWeakest = yourRight
        yourStrongest = yourLeft

    return yourStrongest == myStrongest and yourWeakest == myWeakest

print(are_eqally_strong(10, 15, 15, 10))
print(are_eqally_strong(15, 10, 15, 10))
print(are_eqally_strong(15, 10, 15, 9))
