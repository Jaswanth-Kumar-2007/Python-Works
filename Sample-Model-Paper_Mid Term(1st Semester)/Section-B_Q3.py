def distance(x1,x2,y1,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**(1/2)
    return result

print(distance(3,4,6,8))
