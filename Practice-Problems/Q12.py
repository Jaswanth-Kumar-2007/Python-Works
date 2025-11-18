def prepend(lst):
    lst1 = []
    for i in lst:
        s = "Hi" + str(i)
        lst1.append(s)
    return lst1

lst1 = ["Jaswanth","Kumar"]

#print(prepend(lst1))

def prepend(lst):
    return ["Hi"+ str(x) for x in lst]

print(prepend(lst1))