# Read the input
N = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())

# Create a new array to store the elements within the range
result = []

# Iterate over the array and check if each element is within the range
for num in arr:
    if A <= num <= B:
        result.append(num)

# Display the elements within the range or return -1 if no such elements exist
if len(result) > 0:
    for num in result:
        print(num, end=" ")
else:
    print(-1)
