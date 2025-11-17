pos = 0
neg = 0
zer = 0
lst = []
while True:
    num = int(input("Enter your Number: "))
    lst.append(num)
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zer += 1
    choice = input("Do you want to continue(y/n): ")
    if choice != 'y':
        break

lst1 = sorted(lst)
print(lst1)
if len(lst)%2 != 0:
    print(lst1[int((len(lst1)-1)/2)])