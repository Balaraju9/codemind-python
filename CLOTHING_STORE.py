def countSockPairs(n, arr):
    count = {}
    pairs = 0

    # Count the frequency of each color
    for color in arr:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    # Count the pairs of socks
    for color in count:
        pairs += count[color] // 2

    return pairs

# Get input from the user
n = int(input())
arr = list(map(int, input().split()))

# Count the pairs of socks
pairs = countSockPairs(n, arr)

# Print the number of pairs
print( pairs)
