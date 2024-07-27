# In Python we have a very powerful data structure called Dictionary
# A dictionary is a collection of key value pairs - we use it to map a key to a value
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
# Since dictionaries are collections of key value pairs we can't access items using a numeric index as we do with lists
# print(point["x"]) - will give you 1
# We can change the value of x to a new value
point["x"] = 10
# You can also add a new key
point["z"] = 20
print(point)
# When reading a value - if we use an invalid key we'll get an error
# There are two ways around this
if "a" in point:
    print(point["a"])
# or
print(point.get("a", 0))
# To delete an item we use the del()
del point["x"]
print(point)
# You can also loop over dictionaries
for key in point:  # In each iteration our loop variable will hold the key of an item
    print(key, point[key])
for key, value in point.items():  # In each iteration our loop variable will hold the key of an item
    print(key, value)
