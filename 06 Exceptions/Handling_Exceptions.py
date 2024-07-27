try:
    age = int(input("Age: ")) # We need to put this statement in a try block
except ValueError as ex: #I'm printing ex just for demonstration
    print("You didnt enter a valid age")
    print(ex)
    print(type(ex))
else: #What we have in the else clause will only be executed if there are no exceptions
    print("No exceptions were thrown")

# When python sees a try block it will execute every statement in this block
# -if any of these statements throws an exeption the code in the except clause 
# -will be executed. If we dont have any exceptions, the code will be executed
print("Execution continues")