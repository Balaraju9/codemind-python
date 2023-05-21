def sortedSquares(A):
    # Square each number in the array
    squares = [num ** 2 for num in A]

    # Sort the squared numbers in non-decreasing order
    squares.sort()

    return squares

# Get input from the user
n = int(input())
A = list(map(int, input().split()))

# Call the sortedSquares function to get the resulting array
result = sortedSquares(A)

# Print the resulting array
print(*result)
