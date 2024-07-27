count = 0
for number in range(1, 100):  # for every number in range 1-100
    if number % 2== 0:  # If the remainder of this number is 0(even number)
        count += 1 #Everytime we find an even number we need to increment count
print(f"We have {count} even numbers")



