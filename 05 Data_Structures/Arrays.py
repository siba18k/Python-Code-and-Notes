from array import array
numbers = array("i", [1, 2, 3])
numbers[0] = 1
# You can access items the same way you access them in lists
# But since we used "i" - if you input a float or any other object you will get an error
# If you are dealing with a large sequence of numbers use Arrays
# You will see the difference only if you are dealing with a large
# A typecode is a string of one character that determines the type of objects in your list
print(numbers[0])
