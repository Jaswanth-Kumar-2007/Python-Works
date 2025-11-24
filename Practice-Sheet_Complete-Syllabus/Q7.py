def isValid(side1,side2,side3):
    if side1 + side2 - side3 > 0 and side1 + side3 - side1 > 0 and side2 + side3 - side1 > 0:
        return True
    else:
        return False

def area(side1 , side2 , side3):
    if isValid(side1,side2,side3):
        s = (side1 + side2 + side3)/2
        p = s * (s-side1) * (s-side2) * (s-side3)
        return p ** (1/2)
    else:
        "Invalid Triangle"

print(isValid(3,4,5))
print(area(3,4,5))
