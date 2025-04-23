#01_double_it


# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Double and print until the value is 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')
