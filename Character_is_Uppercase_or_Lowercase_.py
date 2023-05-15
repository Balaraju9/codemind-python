# Take a character as input from the user
character = input()

# Check if the character is uppercase
if character.isupper():
    print("uppercase alphabet")

# Check if the character is lowercase
elif character.islower():
    print("lowercase alphabet")
else:
    print("not an alphabet")

