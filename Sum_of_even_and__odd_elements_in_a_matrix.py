# Read the input
N, M = map(int, input().split())

# Initialize variables for sum of even and odd elements
sum_even = 0
sum_odd = 0

# Iterate over the matrix rows
for i in range(N):
    row = list(map(int, input().split()))
    
    # Iterate over the row elements
    for element in row:
        # Check if the element is even or odd
        if element % 2 == 0:
            sum_even += element
        else:
            sum_odd += element

# Display the sum of even and odd elements
print(sum_even, sum_odd)
