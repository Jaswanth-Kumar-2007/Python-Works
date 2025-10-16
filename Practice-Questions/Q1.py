def factorial_check(num):
    i = 2
    while num > 1 and num%i == 0:
        num = num//i
        i += 1
    if num == 1:
        return "Number is factorial"
    else:
        return "Number is not factorial"

print(factorial_check(20))