def count_digit(n,d):
    if n == 0:
        return 0
    if n%10 == d:
        return 1 + count_digit(n//10,d)
    else:
        return count_digit(n//10,d)

print(count_digit(50705075,0))