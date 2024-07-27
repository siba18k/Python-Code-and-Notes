successful = True 
for number in range(3):
    print("Attempt")
    if successful:  # Indentation is key once again
        print("Successful")
        break  # You use break to jump out of a loop
else:  # what we put under our else statement will only be executed if this loop completes without an early termination
    print("Attempted 3 times and failed")
