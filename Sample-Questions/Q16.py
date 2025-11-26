def unique_squares(lst):
    return [x**2 for x in set(lst)]

print(unique_squares([1,2,2,3]))