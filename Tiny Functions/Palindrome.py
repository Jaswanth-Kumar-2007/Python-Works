def palindrome(n):
    if type(n) == str:
        s = n.lower()
        if s == s[::-1]:
            return "It is Palindrome"
        else:
            return "It is Not Palindrome"
    elif type(n) == int:
        p = str(n)
        if p == p[::-1]:
            return "It is Palindrome"
        else:
            return "It is not Palindrome"

print(palindrome("Malayalam"))
print(palindrome(12521))
        