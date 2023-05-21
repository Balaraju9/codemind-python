def find_sum_of_elements(arr, A, B):
    sum = 0
    for num in arr:
        if num < A or num > B:
            sum += num
    return sum

# Read the length of the array
N = int(input())

# Read the array elements
arr = list(map(int, input().split()))

# Read the values of A and B
A, B = map(int, input().split())

# Find the sum of elements not existing between A and B
result = find_sum_of_elements(arr, A, B)

# Display the sum
print(result)
