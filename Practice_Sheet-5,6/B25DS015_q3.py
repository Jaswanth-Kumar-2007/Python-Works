def isLeapYear(y):
    #Return True if ’year’ is a leap year according to Gregorian rules
    if y%400 == 0 or (y%100 != 0 and y%4 == 0):
        return True
    else:
        return False
    
def isValidDate(y,m,d):
    '''
    Return True if ’year’, ’month’, and ’day’ form a valid date on
    the Month must be 1..12 and day must be valid
    for that month (including month 2)
    '''
    if isLeapYear(y):
        if(m in [1,3,5,7,8,10,12]):
            if d <= 31 :
                return True
            else:
                return False
        elif(m in [4,6,9,11]):
            if d <= 30:
                return True
            else:
                return False
        elif(m == 2):
            if d <= 29:
                return True
            else:
                return False
        else:
            return False   
    else:
        if(m in [1,3,5,7,8,10,12]):
            if d <= 31 :
                return True
            else:
                return False
        elif(m in [4,6,9,11]):
            if d <= 30:
                return True
            else:
                return False
        elif(m == 2):
            if d <= 28: 
               return True
            else:
               return False
        else:
            return False

#Test Cases:
#print(isValidDate(1999,12,31))
#print(isValidDate(2001, 2, 29))     
            
        