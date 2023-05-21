def findGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Get input from the user
num1,num2=map(int,input().split())

# Find the GCD of the given numbers
gcd = findGCD(num1, num2)

# Print the GCD
print(gcd)
