def fizz_buzz(input):
    # The key is to put this condition first because Python interpreter will stop once the condition is true
    # Always put % (Number) == 0, in order to represent as a whole number
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(5))
