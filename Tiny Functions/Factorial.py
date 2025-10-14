def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res

ans = []
for i in range(1,20):
    ans.append(factorial(i))

print(ans)