try:
    age = int(input("Age: ")) # We need to put this statement in a try block
    xfactor = 10/age #If you put 0 the program will crash because you cannot divide by 0
except (ValueError,ZeroDivisionError):# Better than add the another execption block below add the several exception between paranthesis.
    print("You didnt enter a valid age")
else:
    print("No exceptions were thrown")
    # *In the try: block - If any of the statements throws an exception that matches one of the 
    # except clauses that except clause is executed and the others are ignored
print("Executions continues") # Because we are handeling this exeption properly the line will be executed, and the program will not crash