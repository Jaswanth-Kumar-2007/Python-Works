a = int(input("Enter your a: "))
b = int(input("Enter your b: "))
try:
    c = (a+b)/(a-b)
    print(c)
except:
    print("ZeroDivisonError")


