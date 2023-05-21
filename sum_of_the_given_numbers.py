# Read the value of N
N = int(input())

# Iterate over N lines
for _ in range(N):
    # Read the pair of numbers
    a, b = map(int, input().split())
    
    # Calculate the sum
    sum = a + b
    
    # Print the sum
    print(sum)
