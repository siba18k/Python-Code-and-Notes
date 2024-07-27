def multiply(*numbers): # With an * before the parameter we can add multiple arguments to create a Tuple
    total = 1
    for number in numbers:
        total *= number #Or total = number * total
    return total
# Make sure that the indentation for "return" should be at the lines of indentation as "for" otherwise it will become part
#  of the loop and will return something completetly different
print(multiply(2,3,4,5))
