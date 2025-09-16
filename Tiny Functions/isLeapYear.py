def isLeapYear(y):
    if y%400 == 0 or (y%100 != 0 and y%4 == 0):
        return True
    else:
        return False
    
print(isLeapYear(1956))