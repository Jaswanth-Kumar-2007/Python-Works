def pythagorean_triplets(n):
    res = []
    for c in range(n):
        for b in range(c):
            for a in range(b):
                if a**2 + b**2 == c**2:
                    s = [a,b,c]
                    res.append(s)
        
    return res,len(res)                   
                    
print(pythagorean_triplets(30))