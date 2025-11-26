def prime_numbers(n):
    return [i for i in range(2,n)  if all(i % j != 0 for j in range(2,i))]

print(prime_numbers(100))