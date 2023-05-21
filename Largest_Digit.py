def findLargestDigit(n):
    largest = -1  # Initialize largest as a small value

    # Iterate over each digit in the number
    while n > 0:
        digit = n % 10  # Extract the rightmost digit
        if digit > largest:
            largest = digit
        n //= 10  # Remove the rightmost digit

    return largest

# Get input from the user
n = int(input())

# Find the largest digit
largest_digit = findLargestDigit(n)

# Print the result
print(largest_digit)
