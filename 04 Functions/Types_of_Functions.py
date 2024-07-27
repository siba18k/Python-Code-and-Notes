def greet(name):
    print(f"Hi {name}")

# We have 2 types of functions in  programming:
# 1-Perform a task
# 2-That return a value


def get_greeting(name):
    return f"Hi {name}"  # We use return to return a value from this function


message = get_greeting("Sibahle")
file = open("Functions\content.txt", "w")
file.write(message)
