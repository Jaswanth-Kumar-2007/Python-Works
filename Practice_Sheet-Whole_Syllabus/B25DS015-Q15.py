def square_of_evens(numbers):
    res = []
    for i in numbers:
        if i%2 == 0:
            res.append(i**2)
    return res

print(square_of_evens([1,2,3,4,5]))
print(square_of_evens([1,3,5]))