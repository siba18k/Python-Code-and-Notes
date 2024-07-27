# for x in range(5):
#     In each iteration we get x multiplied by 2 and add it to our list
#     values.append(x*2)
# print(values)

# [expression for item in items]
# This is an example of a dictionary comprenshion
values = [x * 2 for x in range(5)]
# This line of code is exactly the same as lines 1 - 4
# This is also not limited to lists
# It also works for sets,lists and dictionaries
values = {x * 2 for x in range(5)}
# In both sets and dictionaries we use "{}"
# In sets we just have values
# In dictionaries we have key value pairs that are separated using a ":"
# e.g {1:"a",2:"b"}
values = {x: x * 2 for x in range(5)}  # It also works for sets
print(values)
