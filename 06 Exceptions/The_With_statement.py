try:
    with open("E:\PythonDev Stuff\HelloWorld\Exceptions\App.py") as file:
        print("File Opened.")
        # The with statement is used to automatically releases exernal resources so you dont have to use .close()
        age = int(input("Age: ")) 
        xfactor = 10/age 
except (ValueError,ZeroDivisionError):
    print("You didnt enter a valid age")
else:
    print("No exceptions were thrown")
# If an object as this two methods we say that object supports context management protocol.
# And we can use it with the "with" statment. And Python will automatically call the exit method and realese external resourses
# file.__enter__
# file.__exit__

# Some times we can be working the several files
# with open("05 The With Statement.py") as file, open("04 Cleaning Up.py") as file2: