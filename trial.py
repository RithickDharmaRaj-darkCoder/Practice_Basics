# practice section...

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 2) or (row == 0) or (row == 6 and column < 2) or (column == 0 and row == 5):
                print(f" {sq} ",end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
