def quotient_remainder(a,b):
    m = 0
    q = 0
    while m<a:
        m = m+b
        q = q+1
        r = a-q*b
    else:
        if m == a:
            r = 0
        else:
            r = a-(q-1)*b
    return q-1,r

#print(quotient_remainder(19,17))