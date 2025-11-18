def capcheck(str,sum=0):
    lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if str == "":
        return sum
    if str[0] in lst:
        sum += 1
    return capcheck(str[1:],sum)


#print(capcheck("aPpleB"))

def capcheck(str):
    if str == "":
        return 0
    if str[0].isupper():
        return 1 + capcheck(str[1:])
    else:
        return capcheck(str[1:])

print(capcheck("AppLeB"))