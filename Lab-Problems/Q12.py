def binaryToHex(binaryValue):
    sum = 0
    l = len(binaryValue)
    p = binaryValue[::-1]
    for i in range(l):
        sum += int(p[i]) * (2**i)
    n = sum
    dic = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if n == 0:
        return str(0)
    elif n < 0:
        return "Error Value"
    else:
        p = str()
    while n != 0:
        s = n%16
        p = p + str(dic[s])
        n = n//16
    return p[::-1]  

print(binaryToHex('11111111')) 