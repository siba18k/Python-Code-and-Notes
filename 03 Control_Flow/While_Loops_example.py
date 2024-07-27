command = ""
while command.lower() != "quit":  # In this way it's doesnt matter how the user type the word quit, it will alway terminate the program
    command = input(">")
    print("ECHO", command)
