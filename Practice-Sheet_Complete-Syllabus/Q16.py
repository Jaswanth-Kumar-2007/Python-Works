from typing import List

def isConsecutiveFour(values):
    if len(values) == 1 and len(values[0]) > 1:
        n = len(values[0])
        for i in range(n):
            if values[0][0] != values[0][i]:
                return False
        return True
    elif len(values) > 1 and len(values[0]) == 1:
        n = len(values)
        for i in range(n):
            if values[0] != values[i]:
                return False
        return True
    elif len(values) > 1 and len(values[0]) > 1:
        if len(values) == len(values[0]):
            n = len(values)
            for i in range(n):
                if values[0][0] != values[i][i]:
                    return False
            return True

print(isConsecutiveFour([[1,1,1,1]]))
print(isConsecutiveFour([[2],[2],[2],[2]]))
values=[
 [1,0,0,0],
 [0,1,0,0],
 [0,0,1,0],
 [0,0,0,1]
 ]
print(isConsecutiveFour(values))
