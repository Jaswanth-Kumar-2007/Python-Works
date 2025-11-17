pos = 0
neg = 0
zer = 0
while True:
    num = int(input("Enter your Number: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zer += 1
    choice = input("Do you want to continue(y/n): ")
    if choice != 'y':
        break

print(f"Positive : {pos} , Negative : {neg} , Zero : {zer}")