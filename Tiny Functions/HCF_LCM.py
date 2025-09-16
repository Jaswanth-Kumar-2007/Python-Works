def remainder(a,b):
    m = 0
    q = 0
    while (m < a):
        m += b
        q += 1
    if m == a:
        return 0
    else:
        return a-(q-1)*b
    
def HCF_LCM(a,b):
    if a>b:
        for i in range(b,0,-1):
            if remainder(a,i) == 0:
                if b%i == 0:
                    lcm = int((a*b)/i)
                    return f"HCF is {i} and LCM is {lcm}"
                else:
                    return f"HCF is 1 and LCM is {a*b}"
    else:
        for i in range(a,0,-1):
            if remainder(b,i) == 0:
                if a%i == 0:
                    lcm = int((a*b)/i)
                    return f"HCF is {i} and LCM is {lcm}"
                else:
                    return f"HCF is 1 and LCM is {a*b}"

print(HCF_LCM(20,5))
print(HCF_LCM(121,11))
        