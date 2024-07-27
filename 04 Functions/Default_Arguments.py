# 05 Default Arguments

# All the parameters that are in the function are required by default, 
# in this lecture we are going make the a parameter optional.
# All the optinal parameters must come after the required parameter
def increment(number, by=1):
    return number + by

# keyword argurments make your code more readable to others
result = increment(2)
print(result)
print(increment(2,6))
