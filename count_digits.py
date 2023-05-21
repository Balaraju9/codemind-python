# Read the input
N = int(input())
arr = list(map(int, input().split()))

# Iterate over the array and count the number of digits in each element
digit_counts = [len(str(abs(num))) for num in arr]

# Display the count of digits for each element
for count in digit_counts:
    print(count, end=" ")
