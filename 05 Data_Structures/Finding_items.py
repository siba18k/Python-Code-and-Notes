letters = ["a", "b", "c"]
if "d" in letters:
    # Since there is no "d" in the list nothing will show
    print(letters.index("d"))


# This will return the number of occurances of the given items on the list
print(letters.count("d"))
