def fortymarks(dic):
    lst = []
    for k,v in dic.items():
        if v < 40:
            lst.append(k)
    return lst

lst1 = {"A":36,"B":45,"C":32}

print(fortymarks(lst1))
