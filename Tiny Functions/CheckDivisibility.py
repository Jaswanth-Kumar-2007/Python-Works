def checkdivisibility(a,b):
    p = a
    while a > 0:
        a = a-b
    if a == 0:
        return f"{p} is divisible by {b}"
    else:
        return f"{p} is not divisible by {b}"
    
print(checkdivisibility(10,3))