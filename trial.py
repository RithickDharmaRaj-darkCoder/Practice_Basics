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
        elif (column == 4 or row == 4):
            print("*", end="  ")
        else:
            print(end="   ")
    print()
