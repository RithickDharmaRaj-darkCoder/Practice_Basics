# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 0) or (column == 4 and ( row == 1 or row == 2)):
                print(f" {sq} ", end="")
            elif ((row == 0 or row == 3) and (0 < column and column < 4) ):
                print(f" {sq} ", end="")
            elif (row == column + 2) and (row > 3) :
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
