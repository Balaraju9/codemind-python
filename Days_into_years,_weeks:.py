# Take the number of days as input from the user
days = int(input())

# Convert days into years and weeks
years = days // 365  # Floor division to get the whole number of years
weeks = (days % 365) // 7  # Remainder division to get the remaining days and then divide by 7 to get the whole number of weeks

# Print the result
print( years)
print(weeks)
