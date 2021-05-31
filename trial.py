# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (row == 0 or row == 3 or row == 6) and (column != 0 and column != 4):
                print(f" {sq} ", end="")
            elif (column == 0 and 0 < row < 3):
                print(f" {sq} ", end="")
            elif (column == 4 and 3 < row < 6) :
                print(f" {sq} ", end="")
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
