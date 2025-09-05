def is_disarium(num):
    #A Disarium number is one where the sum of its digits
    #digits raised to their respective positions equals the number itself"
    l = str(num)
    p = len(l)
    sum = 0
    for i in range(p):
        q = i+1
        sum = sum + int(l[i])**q
    if (sum == int(num)):
        print("True")
    else:
        print("False")

#TestCases:
#is_disarium(175)
#is_disarium(89)
#is_disarium(100)
    