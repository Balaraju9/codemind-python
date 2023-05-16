# Prompt the user to enter two numbers
num1,num2=map(int,input().split())

# Find the maximum of the two numbers
max_num = max(num1, num2)

# Initialize the LCM as the maximum number
lcm = max_num

while True:
    # Check if both numbers are divisible by the current LCM
    if lcm % num1 == 0 and lcm % num2 == 0:
        break

    # Increment the LCM by the maximum number
    lcm += max_num

print(lcm)
