def custom_bool(value):
    '''
    Emulate Python’s built-in bool() without calling it.
    Return Falsenumeric zeros (e.g. 0, 0.0), and
    empty sequences or collections(and True otherwise.
    '''
    if (value == 0 or 0.0 or 0j):
        return False
    elif (value == "" or value == '' or value == None or value == False):
        return False
    elif (value == [] or value == () or value == {} or value == range(0) or value == set()):
        return False
    else:
        return True

#Test Cases:
#print(custom_bool(0)) # False
#print(custom_bool(1)) # True
#print(custom_bool("")) # False
#print(custom_bool("hello")) # True
#print(custom_bool([])) # False
#print(custom_bool([1])) # True
#print(custom_bool(None)) # False