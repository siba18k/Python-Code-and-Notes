age = int(input("Age:" )) # I used int()to convert the input into a number or string to an integer
if age >= 18:  # There is nothing wrong with using print you're still going to get the same result
    message = "Eligible"  # Message is just better
else:
    message = "Not Eligible"

# This is exactly equivalent to the 4 lines of code
# This is called a Ternary Operator
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
