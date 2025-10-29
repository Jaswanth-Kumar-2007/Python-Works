def find_max(numbers):
    if len(numbers) == 0:
        return None
    p = numbers[0]
    for i in numbers:
        if p < i:
            p = i
    return p

print(find_max([1,5,3,9,2]))
print(find_max([-10,-5,-2]))
print(find_max([]))