# String Methods...


for row in range(5):
    print("    ", end="")
    for column in range(5):
        if (column == 0 or row == 4):
            print("*", end="  ")
        elif (row == column):
            print("*", end="  ")
        else:
            print(end="   ")
    print()
