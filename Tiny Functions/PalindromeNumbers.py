def Palindrome_Numbers(a,b):
    res = []
    for i in range(a,b):
        p = str(i)
        if p == p[::-1]:
            print(i)
            res.append(i)
    return res
    
print(Palindrome_Numbers(1000,10000))