def allLongestStrings(list_of_strings):

    longest_strings = []
    max_len = max(list(map(lambda  x: len(x), list_of_strings)))

    for item in list_of_strings:
        if len(item) == max_len:
            longest_strings.append(item)


# Alternative Solution
    """
    longest_strings = []
    max_len = 0
    for item in list_of_strings:
        temp = len(item)
        if len(item) > max_len:
            max_len = len(item)

    for item in list_of_strings:
        if len(item) == max_len:
            longest_strings.append(item)"""

    return longest_strings

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
print(allLongestStrings(["Apple", "House", "Color", "Red", "Boat", "Door"]))