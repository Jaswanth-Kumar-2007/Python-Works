def celtofah(temp):
    return [((x*9)/5)+32 for x in temp]

print(celtofah([15,20]))