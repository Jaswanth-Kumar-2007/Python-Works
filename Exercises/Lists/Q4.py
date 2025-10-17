def median_value(numbers):
    # Create a copy to avoid changing original order
    temp = sorted(numbers)
    n = len(temp)
    mid = n // 2

    # If odd number of elements → middle element
    if n % 2 != 0:
        return temp[mid]
    else:
        # If even → average of middle two
        return (temp[mid - 1] + temp[mid]) / 2

# Example
nums = [5, 1, 9, 3, 7]
print("Median:", median_value(nums))
print("Original list (unchanged):", nums)
