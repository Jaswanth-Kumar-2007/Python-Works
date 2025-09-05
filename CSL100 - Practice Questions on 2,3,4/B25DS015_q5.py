def swap_variables(a,b):
    #Swaps the values of two integer variables without using
    #a third temporary variable.
    a = int(a)
    b = int(b)
    a = a+b
    b = a-b
    a = a-b
    return a , b

#TestCases:
#print(swap_variables(10,20))
#print(swap_variables(5,15))


