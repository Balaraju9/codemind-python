def find_distinct_characters(string):
    distinct_chars = set()
    
    # Convert the string to lowercase for case insensitivity
    string = string.lower()
    
    # Add characters to the set
    for char in string:
        if char.isalpha():  # Consider only alphabetic characters
            distinct_chars.add(char)
    
    # Convert the set to a sorted list
    distinct_chars = sorted(list(distinct_chars))
    
    # Return the distinct characters
    return distinct_chars


# Get the input string from the user
input_string = input()

# Find the distinct characters
distinct_characters = find_distinct_characters(input_string)

# Display the result
print(''.join(distinct_characters))
