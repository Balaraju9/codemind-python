def isAutomorphicNumber(n):
    square = n * n
    original_length = len(str(n))
    square_digits = str(square)[-original_length:]
    
    return int(square_digits) == n

# Get input from the user
n = int(input())

# Check if the number is an automorphic number or not
if isAutomorphicNumber(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
