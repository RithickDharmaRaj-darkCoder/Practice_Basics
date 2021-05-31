# None Data Type

sq = input("Enter one element : ").upper()
if len(sq) == 1:
    r = 0
    c = 6
    for row in range(7):
        print("    ", end="")
        for column in range(7):
            if (row == r and column == c):
                print(f" {sq} ", end="")
                r += 1
                c -= 1
            elif (row == 0 or row == 6):
                print(f" {sq} ", end="")

            else:
                print(end="   ")
        print()
else:
    print("Warning! Enter only '1' Character.")
