def check_armstrong(num):
    num = str(num)
    l = len(num)
    sum = 0
    for i in range(l):
        sum = sum + int(num[i])**l
    if l == 3:
        if sum == int(num):
            return True
        else:
            return False
    else:
        return "Error: Not a 3 digit number"
        return False