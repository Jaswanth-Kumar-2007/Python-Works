def fizzBuzz(n):
    if n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return f"{n} is Not Divisible by 3 or 5"
    
print(fizzBuzz(17))
print(fizzBuzz(171))