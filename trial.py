# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    r = 0
    c = 4
    for row in range(7):
        print("    ", end="")
        for column in range(5):
            if (column == 2 and row > 2):
                print(f" {sq} ", end="")
            elif (row == column) and (row < 3):
                print(f" {sq} ", end="")
            elif (row == r and column == c) and (row < 3):
                print(f" {sq} ", end="")
                r += 1
                c -= 1
            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
