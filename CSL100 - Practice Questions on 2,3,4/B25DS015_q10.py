def print_alphabet_pattern(n):
    #Alpabet Pattern
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = 2*n-1
    s = alphabet[0:l]
    print(s)
    p = 1
    for i in range(n-1):
        print(s[0:n-1-i]+" "*(p)+s[n+i:l])
        p = p+2
    
    
#TestCases:
#print_alphabet_pattern(2)
print_alphabet_pattern(4)    
#print_alphabet_pattern(5)   