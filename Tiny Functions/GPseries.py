def GP(N):
    for i in range(N):
        if i == 0:
            print("a",end = ",")
        elif i == 1:
            print("ar", end = ",")
        else:
            print("a"+"r"*(i),end = ",")
            
GP(3)