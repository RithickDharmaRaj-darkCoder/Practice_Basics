# String Methods...


r = 0
c = 4
for row in range(5):
    print("    ", end="")
    for column in range(5):
        if (row == r and column == c):
            print("*", end="  ")
            r += 1
            c -= 1
        elif (row == 0 or column == 0):
            print("*", end="  ")
        else:
            print(end="   ")
    print()
