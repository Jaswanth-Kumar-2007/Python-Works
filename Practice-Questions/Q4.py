def binary_to_decimal(binary):
    # Base case: if binary is 0 or 1
    if binary == 0:
        return 0
    else:
        # Get last digit (LSB)
        last_digit = binary % 10
        # Remaining binary number
        remaining = binary // 10
        # Recursive formula: decimal = last_digit + 2 * (decimal of remaining)
        return last_digit + 2 * binary_to_decimal(remaining)

# Example
num = 1011
print("Decimal value:", binary_to_decimal(num))
