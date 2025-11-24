def collatzsequence(n):
    while n != 1:
        yield int(n)
        if n %2 == 0:
            n = n/2
        else:
            n = 3*n+1
    yield 1

print(list(collatzsequence(10)))
print(list(collatzsequence(12)))
