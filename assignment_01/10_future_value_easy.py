# Get the desired future value.
future_value = float(input('How many frogs would you like: '))

# Get the annual interest rate.
rate = float(input('Frog "interest" rate: '))

# Get the number of years that the money will appreciate.
years = int(input('How long are you letting the frogs get freaky: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

# Display the amount needed to deposit.
print('You will have this many frogs:', present_value)



