def Upper_List(lst):
    for i in lst[:]:
        lst.append(i.upper())
        lst.remove(i)
    return lst

nums = ["apple","banana","cherry"]
print(Upper_List(nums))