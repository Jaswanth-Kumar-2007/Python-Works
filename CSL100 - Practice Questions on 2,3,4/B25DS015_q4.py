def check_armstrong(num):
    #Checks if a 3 digit number is an Armstrong Number
    #An Armstrong number is one where the sum of its digits
    #cubed equals the number itself
    #Prints an error for non 3 digit numbers
    num = str(num)
    l = len(num)
    sum = 0
    for i in range(l):
        sum = sum + int(num[i])**l
    if l == 3:
        if sum == int(num):
            print("True")
        else:
            print("False")
    else:
        print("Error: Not a 3 digit number")
        print("False")
        
    
 
#TestCases:
#check_armstrong(371)
#check_armstrong(300)
#check_armstrong(99)
    
    
        