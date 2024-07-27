items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
x = list(filter(lambda item: item[1] >= 10, items))
print(x)

#  Refer to List_Comprehensions.py for the better/easier way of doing this.
