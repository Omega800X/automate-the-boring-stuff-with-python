# Empty string is treated as False, non-empty strings are treated as True
# Integers: 0 is falsey, all others are truthy
# Floats: 0.0 is falsey, all others are truthy
# It is better to write conditions in a clearer way like name != ''
print('Enter a name.')
name = input()
if name: 
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')