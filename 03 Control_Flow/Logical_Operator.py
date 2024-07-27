# We have 3 logical operators in python:
# and - If both conditions are true, the result will be true
# or - if atleast one condition will be true, the result will be true
# not - inverses the value of a boolean (Turns "True" to "False")
# These are all useful for real world applications
high_income = True
good_credit = True
student = False

# if high_income and good_credit:  # Putting "True" here will make your code redundant 
# -because it's the variables are either true or false
print("Eligible")
# else:
print("Not Eligible")
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
