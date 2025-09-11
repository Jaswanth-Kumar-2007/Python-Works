def SwapNumber_Without_TempVariable(a,b):
    a = a+b
    b = a-b
    a = a-b
    return f"{a},{b}"

print(SwapNumber_Without_TempVariable(3,4))
    