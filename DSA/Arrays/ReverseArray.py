def reverse_array(arr):
    res = []
    for i in arr[::-1]:
        res.append(i)
        
    for j in range(len(arr)):
        arr[j] = res[j]
    return arr
    
        
print(reverse_array([2,5,4]))
print(reverse_array([1,2,3,4,5,6,7]))
    