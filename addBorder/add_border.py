

def add_border(picture):
    
    wall = "*" * (len(picture[0]) +2)

    picture.insert(0, wall)
    picture.insert(len(picture), wall)
 
    for i in range(1 ,len(picture)-1):
        picture[i] = "*" + picture[i] + "*"
    return picture
    

print(*add_border(["abcdef", "abcdef","abcdef"]), sep='\n')

