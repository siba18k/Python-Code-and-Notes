# # An exception is a kind of error that terminates the execution of program
# numbers = [1,2]
# print(numbers[3])


# int(input("Age: ")) 
# As a programmer you're supposed to prevent your programs from crashing 
# (All these are just sxample btw - they won't work properly)


# Errors detected during execution are called exceptions.

# Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# Built-in Exceptions
# https://docs.python.org/3/library/exceptions.html

# numbers = [1, 2]
# print(number[3])

# With this program we get an error because de list does not have index 3
# File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\01 Exceptions.py", line 10, in <module>
#     print(numnbers[3])
# IndexError: list index out of range
try:
    age = int(input("Age: "))
    if age <= 18:
        print("You're still young blud")
    elif age >= 19:
        print("You are finally of age ")
    elif age >= 30:
        print("You lowkey pushing it")
    elif age >= 40:
        print(f"Time to stop clubbing chief.\n Go start a family")
    elif age >= 50:
        print("Go see your Grandkids")
except ValueError:
    print("You didnt enter a valid age")
except TypeError:
    print("My fault OG")
else:
    print('No exceptions')

# With this code we will get an error if we enter a non-numeric value
# File "c:/Users/jmigu/iCloudDrive/Os meus documentos/Educação/Code with Mosh/The Complete Python Course/HelloWorld/06 Exceptions (20m)/01 Exceptions.py", line 17, in <module>
#     age = int(input("Age: "))
# ValueError: invalid literal for int() with base 10: 'a'