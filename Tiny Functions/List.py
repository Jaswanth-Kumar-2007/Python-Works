#Create a List
lst = []
for i in range(20):
    lst.append(i)
print(lst)

#Finding an Element in List
print(1 in lst)

#Slicing of List
print(lst[1:18])

#Adding elements to the list
lst1 = ['A','B','C','D','E','F','G','H']
lst1.append('I')
print(lst1)
l = len(lst1)
lst1.insert(l,'I')
print(lst1)
lst1.extend(lst)
print(lst1)

#Removing elements from List
lst1.remove('A')
print(lst1)
lst1.pop(0)
print(lst1)

lst[3:5] == [210,211]
print(lst)

list_2 =[10,20,30,40,50,60]
list_2[4] = 70
print(list_2)

list_2[1:4] = [12,14,16]
print(list_2)

#Sorting a List
lst.sort()

def sort_numbers(nums):
    res = []
    while nums != []:
        p = nums[0]
        for i in nums:
            if i < p:
                p = i
        res.append(p)
        nums.remove(p)
    return res

lst_3 = [2,4,6,3,7,4,1,3]
print(sort_numbers(lst_3))

#Reverse Numbers
lst_3.reverse()
print(lst_3)

def reverse_numbers(nums):
    nums[::-1]
    return nums

print(reverse_numbers(lst_3))
