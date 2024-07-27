letters = ["a", "b", "c"]

# Add an item
letters.append("d")
letters.insert(0, "-")
print(letters)

# Removing an item:

# We can also add an index here in order to be more specific (will only delete one item)
letters.pop(0)
print(letters)

# You can use this if you do not know the exact index number of what you need to remove
letters.remove("b")
print(letters)

# Delete can be used to delete a range of items
# we can also delete an item by using an index and also delete a range of items by using an index
del letters[0:3]
print(letters)

# If you want to delete all the items on a list use the clear method
letters.clear()
print(letters)
