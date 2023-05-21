def isAdamNumber(n):
    # Calculate the square of n
    square_n = n ** 2

    # Calculate the reverse of n
    reverse_n = int(str(n)[::-1])

    # Calculate the square of the reverse of n
    square_reverse_n = reverse_n ** 2

    # Check if the square of n and square of the reverse of n are reverse of each other
    return str(square_n) == str(square_reverse_n)[::-1]

# Get input from the user
n = int(input())

# Check if the number is an Adam number
is_adam = isAdamNumber(n)

# Print the result
print(is_adam)
