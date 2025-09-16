def reverse_list(lst):
    l = len(lst)
    left = 0
    right = l-1
    while left < right:
        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        right -= 1
    return lst

print(reverse_list([1,2,3,4,5,6]))
    