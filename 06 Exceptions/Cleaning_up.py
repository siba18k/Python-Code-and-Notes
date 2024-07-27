try:
    file = open("App.py")
    age = int(input("Age: ")) # We need to put this statement in a try block
    xfactor = 10/age #If you put 0 the program will crash because you cannot divide by 0
except (ValueError,ZeroDivisionError):
    print("You didnt enter a valid age")
else:
    print("No exceptions were thrown")
finally:#We use the finally clause to prevent redundancy in our code
    file.close()
# The finally clause is always executed no matter whether we have an exception or not 