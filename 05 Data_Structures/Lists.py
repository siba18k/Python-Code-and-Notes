# [] - Define a list or  sequence of objects
letters = ["a", "b", "c"]
# We can also have lists inside of lists
matrix = [[0, 1], [2, 3]]  # This is called a matrix(A two-dimensional list)
zeros = [0] * 5  # using a "*" we can repeat iems in a list
# We can use a "+" to concatenate multiple lists
combined = zeros + letters
# list() takes an itterable and converts it to list
numbers = list(range(1, 21))
chars = list("Hello World")  # Strings are also iterable(can be looped over )
# Each item in our original string is an item in this list
print(chars)
print(len(chars))
print(numbers)
