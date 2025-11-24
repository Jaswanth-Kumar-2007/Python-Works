try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("This will always run.")
