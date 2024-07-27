# Scope refers to the region of the code where the variable is defined

# This is now a global variable - Long Lifetime (Evil - Avoid Global at all costs)
message = "a"


def greet(name):  # The slope of the variable is the greet function
    message = "b"  # This is a local variable - Short lifetime(Good)


greet("Siba")
print(message)
# print(message) will not work here because greet() is a local variable in this instance
