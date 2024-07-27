# We can put one loop inside of another loop
for x in range(4):  # This is the outer loop (Parent), 0 is the first iteration of the outer loop and 3 is the last
    for y in range(4):  # This is the inner loop(Child), what we have in here will be executed 3 times
        for z in range(5):  # This is just something extra I did
            print(f"({x},{y},{z})")
