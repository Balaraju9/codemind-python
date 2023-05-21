def smallerNumbersThanCurrent(nums):
    # Count the occurrence of each number
    count = [0] * 101
    for num in nums:
        count[num] += 1
    
    # Calculate the prefix sum of the count array
    prefix_sum = [0] * 101
    prefix_sum[0] = count[0]
    for i in range(1, 101):
        prefix_sum[i] = prefix_sum[i-1] + count[i]
    
    # Calculate the number of smaller numbers for each element
    result = [0] * len(nums)
    for i, num in enumerate(nums):
        if num == 0:
            result[i] = 0
        else:
            result[i] = prefix_sum[num-1]
    
    return result

# Get input from the user
n = int(input())
nums = list(map(int, input().split()))

# Call the smallerNumbersThanCurrent function to get the result
result = smallerNumbersThanCurrent(nums)

# Print the result
print(*result)
