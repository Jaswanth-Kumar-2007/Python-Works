def AP(N):
    for i in range(N):
        if i == 0:
            print("a",end = ",")
        elif i == 1:
            print("a + b", end = ",")
        else:
            print(f"a + {i}b",end = ",")
            
AP(3)