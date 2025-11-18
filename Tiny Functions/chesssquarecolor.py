def chesssquare(x,y):
    if x%2 == 0 and y%2 == 0:
        return "White"
    elif x%2 != 0 and y%2 != 0:
        return "White"
    else:
        return "Black"

print(chesssquare(1, 1))
print(chesssquare(2, 1))
print(chesssquare(1, 2))
