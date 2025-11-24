def prime_generator(n):
    if n == 0:
        return []
    else:
        res = [2]
        i = 3
        while len(res) != n:
            s = True
            for j in range(i-1,1,-1):
                if i % j == 0:
                    s = False
            if  s:
                res.append(i)
            i += 1
        return res

print(prime_generator(5))
print(prime_generator(10))
        


