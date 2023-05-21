import math

def isPerfectSquare(n):
    root = math.sqrt(n)
    return root.is_integer()

# Get input from the user
n = int(input())

# Check if the number has a perfect square root
if isPerfectSquare(n):
    print("True")
else:
    print("False")
