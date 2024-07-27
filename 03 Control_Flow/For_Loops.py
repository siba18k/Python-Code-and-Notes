# There are times we may want to repeat a task a number of times
# We use loops to create repetition
# for every number in the range(start,finish before,step[optional]) the word "Attempt" will be printed
for number in range(1, 10, 2):
    # The string(".") will be multiplied by the number that number of times
    print("Attempt", number, (number)*".")
