# Read the input
N = int(input())
arr = list(map(int, input().split()))

# Create a new array to store the reversed elements
reversed_arr = []

# Iterate over the array and reverse each element
for num in arr:
    reversed_num = int(str(num)[::-1])  # Reverse the number using string slicing
    reversed_arr.append(reversed_num)

# Display the reversed array
for num in reversed_arr:
    print(num, end=" ")
