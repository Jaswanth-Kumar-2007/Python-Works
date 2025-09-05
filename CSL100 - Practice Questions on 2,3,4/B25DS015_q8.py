def construct_number(N):
    e = 10**(N-1)
    f = 10**N
    print(e)
    print(f)
    for i in range(e,f):
        if (i % 3 == 0):
            if (i % 9 != 0):
                if (i % 10 != 0):
                    print(i)
                    break
                

    
