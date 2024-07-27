letters = ["a", "b", "c", "d"]
# print(letters[0])  # This will return the first item in this list
# If we put [-1] it will return the last value/ first value from the end of the list (Similar to strings)
# [0] for first
# [-1] for last
letters[0] = "A"  # Using [] we can also modify items in the list
# print(letters[0:3])  # We can use an index to slice up a string
# When we slice up a string, we can also use steps to return, for example, every second value in a list
# print(letters[::2])
numbers = list(range(20))
print(numbers[::2])  # This wil give you all the even numbers
# This will return all of the numbers(items) on the list in reverse order
print(numbers[::-1])
