#welcome message 
print("Welcome to our Calculator")

#  user input for the first number
X = float(input("Enter the first number: "))

# Take user input for the second number
Y = float(input("Enter the second number: "))

# Ask the user to select either addition (+) or subtraction (-)
Sign = input("Select - or +: ")

# Check if the selected operation is addition
if Sign == "+":
    # If it's addition, perform addition and store the result in the variable Sum
    Sum = X + Y
else:
    # If it's not addition, assume it's subtraction and perform subtraction,
    # then store the result in the variable Sum
    Sum = X - Y

# Print the result of the calculation
print("Result:", Sum)
