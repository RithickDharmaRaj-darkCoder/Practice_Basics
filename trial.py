# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if ((column == 0 or column == 4) and (row != 6 and row != 5)):
                print(f" {sq} ", end="")
            elif (row == 6 and column == 2):
                print(f" {sq} ", end="")
            elif (row == 5 and (column == 1 or column == 3)):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
