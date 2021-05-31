# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(8):
        print("    ", end="")
        for column in range(6):
            if ((column == 0 or column == 4) and (row != 0 and row != 6 and row != 7)):
                print(f" {sq} ", end="")
            elif ((row == 0 or row == 6) and (0 < column and column < 4)):
                print(f" {sq} ", end="")
            elif ((row == column+2) and (column>1)) or (column == 1 and row == 4 ):
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
