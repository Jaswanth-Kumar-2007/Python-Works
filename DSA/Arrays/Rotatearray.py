def rotatearray(arr,d):
    n = len(arr)
    d = d%n
    temp = arr[d:] + arr[:d]
    
    for i in range(n):
        arr[i] = temp[i]
        
    return arr

print(rotatearray([1,2,3,4,5],2))