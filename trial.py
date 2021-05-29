# practice section...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    r = 0
    c = 4
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0 or column == 4):
                print(f" {sq} ",end="")
            elif (row == 1 and column != 2) or (row == 2 and column == 2):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
