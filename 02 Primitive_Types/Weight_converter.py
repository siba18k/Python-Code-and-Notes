
weight = float(input('Weight : '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Pounds: " + str(converted) + " "+"lbs")
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kilograms: " + str(converted) + " "+"kg")
