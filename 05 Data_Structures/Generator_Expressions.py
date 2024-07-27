# A generator expression is a compact generator notation in parentheses:
# generator_expression ::=  "(" expression comp_for ")"
# A generator expression yields a new generator object.
# Its syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of brackets or curly braces.

# Unlike list they don't store all the values in the memory, they generate a value in each interation.


from sys import getsizeof
# This will take only 104 bytes of memory - good
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
# Just be aware that generator objects don't store all the items in memory 
# - you won't be able to get the total number of items you are working with
# print(values)
# for x in values:
#     print(x)
# Generator objects are iterable and we can iterate over them and in each iteration they generate a new value
# Unlike lists - they don't store all the values in memory
# This will take 800984 bytes of memory - bad
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
