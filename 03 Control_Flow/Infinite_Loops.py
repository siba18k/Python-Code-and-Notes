# an infinite Loop is a loop that runs forever
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break  # Now there is no need for (command = "")
    # Be aware of infinite loops
    # You should always have a way to jump out of them otherwise your program may run out of memory and crash
