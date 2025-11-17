def pythagoreantriplet(a,b,c):
    if a**2+b**2-c**2 == 0 or a**2+c**2-b**2 == 0 or b**2+c**2-a**2 == 0:
        return True
    else:
        return False

print(pythagoreantriplet(3,4,5))