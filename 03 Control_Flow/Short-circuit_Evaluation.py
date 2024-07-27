high_income = True
good_credit = True
student = False

# The evalution stops as soon as of these arguments are false
if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# The evaluation stops as soon as one of the arguments are true
if (high_income or good_credit) or not student:
    print("Eligible")
else:
    print("Not Eligible")
