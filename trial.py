# String Methods...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(5):
        print("    ", end="")
        for column in range(5):
            if (column == 4) or (row == 0):
                print(f" {sq} ", end="")
            elif (row == column):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")