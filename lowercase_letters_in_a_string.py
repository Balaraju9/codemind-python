# Read the input
string = input()

# Initialize a counter variable
count = 0

# Iterate over each character in the string
for char in string:
    if char.islower():
        count += 1

# Display the count of spaces
print(count)
