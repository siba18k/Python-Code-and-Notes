def save_user(**user):  # When we use ** we can pass multiple arguments and multiple key value pairs/ key value options 
    # and python will automatically package them into a dictionary
    print(user["name"])


save_user(id=1, name="John", age=22)
