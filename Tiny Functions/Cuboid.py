def cuboid(n):
    print(" "*(n+1) + "+" + "-"*2*n + "+")
    for i in range(n,0,-1):
        print(" "*i + "/" + " "*2*n + "/"+ " "*(n-i) +"|")
    print("+" + "-"*2*n + "+"+" "*n + "+")
    for p in range(1,n+1):
        print("|" + " "*2*n + "|" +" "*(n-p) + "/")
    print("+" + "-"*2*n + "+")
    
cuboid(1)
cuboid(2)
cuboid(5)