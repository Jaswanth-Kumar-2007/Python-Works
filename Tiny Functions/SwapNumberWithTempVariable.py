def SwapNumber_With_TempVariable(a,b):
    s = a
    a = b
    b = s
    return f"{a},{b}"

print(SwapNumber_With_TempVariable(3,4))
    