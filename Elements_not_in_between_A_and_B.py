def find_elements_not_existing(arr, A, B):
    result = []
    for num in arr:
        if num < A or num > B:
            result.append(num)
    return result

# Read the length of the array
N = int(input())

# Read the array elements
arr = list(map(int, input().split()))

# Read the values of A and B
A, B = map(int, input().split())

# Find the elements not existing between A and B
result = find_elements_not_existing(arr, A, B)

# Display the elements
if result:
    print(" ".join(map(str, result)))
else:
    print(-1)
