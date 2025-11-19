from typing import List

def displayPattern(n):
    res = []
    for i in range(1,n+1):
        s = str()
        for j in range(1,i+1):
            s = s + " " + str(j)
        res.append(s[::-1])
    return res

print(displayPattern(5))

