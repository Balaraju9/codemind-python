def add_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Taking input from the user
num = int(input())

# Calculating the result
result = add_digits(num)

# Printing the result
print(result)
