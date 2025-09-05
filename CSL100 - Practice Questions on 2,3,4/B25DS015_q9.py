import math
def calculate_angles(a,b,c):
    #Given three sides a, b, c, calculates the three angles
    #A, B, C of the triangle. Each angle should be rounded
    #up to the next integer (’ceil’)
    cosA = (b**2 + c**2 - a**2)/(2*b*c)
    if cosA > 1 or cosA < -1 :
        return None
    else:
        r1 = math.acos(cosA)
        d1 = math.degrees(r1)
        A = math.ceil(d1)
    
    
    cosB = (a**2 + c**2 - b**2)/(2*a*c)
    if cosB > 1 or cosB < -1 :
        return None
    else:
        r2 = math.acos(cosB)
        d2 = math.degrees(r2)
        B = math.ceil(d2)
    
    cosC = (a**2 + b**2 - c**2)/(2*b*a)
    if cosC > 1 or cosC < -1 :
        return None
    else:
        r3 = math.acos(cosC)
        d3 = math.degrees(r3)
        C = math.ceil(d3)
    return (A,B,C)

#TestCases:
#print(calculate_angles(3,4,5))
#print(calculate_angles(3,3,3))
#print(calculate_angles(1,1,3))
    