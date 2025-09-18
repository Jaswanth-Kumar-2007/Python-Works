def number_triangle(n):
    p = 0
    r = 1
    s = 1
    while p != n:
        for i in range(s,s+r):
            print(i,end = " ")
        print("")
        s += r
        r += 1
        p += 1
        
    
number_triangle(20)
            
        
            