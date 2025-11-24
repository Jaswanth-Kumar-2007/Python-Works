import math

def area_polygon(n,side):
    if n > 3:
        area = (n * side**2) / (4 * math.tan(math.pi / n))
        return area
    else:
        return "ValueError"

print(area_polygon(5,4))