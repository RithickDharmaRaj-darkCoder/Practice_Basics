# practice section...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    r = 0
    c = 4
    for row in range(7):
        print("    ", end="")
        for column in range(7):
            if (column == 0 or column == 6):
                print(f" {sq} ",end="")
            elif (row == column):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
