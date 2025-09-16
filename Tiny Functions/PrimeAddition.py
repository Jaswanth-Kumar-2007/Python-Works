def primeaddition(x):
    plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for a in plist:
        for b in plist:
            for c in plist:
                if a + b + c == x:
                    return a,b,c
    else:
        return "No Possible Primes"
    
print(primeaddition(5))
        