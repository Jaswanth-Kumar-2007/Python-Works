def capcheck(str,sum=0):
    lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if str == "":
        return sum
    if str[0] in lst:
        sum += 1
    return capcheck(str[1:],sum)


print(capcheck("aPpleB"))